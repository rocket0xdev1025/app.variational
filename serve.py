"""Static server with the same paths as Omni."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGES = {
    "/",
    "/markets",
    "/points",
    "/rewards",
    "/leaderboard",
    "/competition",
    "/trader-rewards",
    "/announcements",
}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        bare = path.rstrip("/") or "/"
        if bare in PAGES or bare.startswith("/perpetual/") or bare.startswith("/swap/"):
            self.path = "/index.html"
        return super().do_GET()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "4173"))
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"http://127.0.0.1:{port}")
    server.serve_forever()
