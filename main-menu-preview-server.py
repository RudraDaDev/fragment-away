from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
FILES = {
    "/": (ROOT / "main-menu-preview.html", "text/html; charset=utf-8"),
    "/main-menu-preview.html": (ROOT / "main-menu-preview.html", "text/html; charset=utf-8"),
    "/assets/backgrounds/main-menu-golden-field.png": (
        ROOT / "assets/backgrounds/main-menu-golden-field.png",
        "image/png",
    ),
}


class PreviewHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        entry = FILES.get(urlsplit(self.path).path)
        if entry is None:
            self.send_error(404)
            return

        file_path, content_type = entry
        if not file_path.is_file():
            self.send_error(404)
            return

        size = file_path.stat().st_size
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(size))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()

        try:
            with file_path.open("rb") as source:
                self.wfile.write(source.read())
        except (BrokenPipeError, ConnectionResetError):
            pass

    def log_message(self, format_string, *args):
        print(f"{self.client_address[0]} - {format_string % args}")


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 8000), PreviewHandler)
    print("Root main menu preview listening on 0.0.0.0:8000")
    server.serve_forever()
