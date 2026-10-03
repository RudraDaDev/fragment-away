from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
FILES = {
    "/": (ROOT / "main-menu-preview.html", "text/html; charset=utf-8"),
    "/main-menu-preview.html": (ROOT / "main-menu-preview.html", "text/html; charset=utf-8"),
    "/assets/backgrounds/main-menu-golden-field.png": (
        ROOT / "assets/backgrounds/main-menu-golden-field.png",
        "image/png",
    ),
    "/assets/videos/main-menu-wind-6s.mp4": (
        ROOT / "assets/videos/main-menu-wind-6s.mp4",
        "video/mp4",
    ),
    "/assets/videos/golden-field-wind-8s.mp4": (
        ROOT / "assets/videos/golden-field-wind-8s.mp4",
        "video/mp4",
    ),
}


class PreviewHandler(BaseHTTPRequestHandler):
    def _serve(self, include_body):
        route = urlsplit(self.path).path
        entry = FILES.get(route)
        if entry is None:
            self.send_error(404)
            return

        file_path, content_type = entry
        if not file_path.is_file():
            self.send_error(404)
            return

        size = file_path.stat().st_size
        start = 0
        end = size - 1
        status_code = 200
        range_header = self.headers.get("Range")

        if range_header and content_type == "video/mp4":
            match = re.fullmatch(r"bytes=(\d*)-(\d*)", range_header.strip())
            if not match:
                self.send_error(416)
                return
            first, last = match.groups()
            if first:
                start = int(first)
                end = int(last) if last else size - 1
            elif last:
                suffix_length = int(last)
                start = max(0, size - suffix_length)
                end = size - 1
            if start >= size or end < start:
                self.send_response(416)
                self.send_header("Content-Range", f"bytes */{size}")
                self.end_headers()
                return
            end = min(end, size - 1)
            status_code = 206

        length = end - start + 1
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(length))
        self.send_header("X-Content-Type-Options", "nosniff")
        if content_type == "video/mp4":
            self.send_header("Accept-Ranges", "bytes")
            if status_code == 206:
                self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.end_headers()

        if not include_body:
            return

        try:
            with file_path.open("rb") as source:
                source.seek(start)
                remaining = length
                while remaining:
                    chunk = source.read(min(64 * 1024, remaining))
                    if not chunk:
                        break
                    self.wfile.write(chunk)
                    remaining -= len(chunk)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def do_GET(self):
        self._serve(include_body=True)

    def do_HEAD(self):
        self._serve(include_body=False)

    def log_message(self, format_string, *args):
        print(f"{self.client_address[0]} - {format_string % args}")


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 8000), PreviewHandler)
    print("Root main menu preview listening on 0.0.0.0:8000")
    server.serve_forever()
