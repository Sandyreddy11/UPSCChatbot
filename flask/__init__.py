class Request:
    def __init__(self, data=None):
        self._data = data or {}

    def get_json(self):
        return self._data

class Response:
    def __init__(self, json):
        self._json = json
        self.status_code = 200

    def get_json(self):
        return self._json

def jsonify(data):
    return data

class Flask:
    def __init__(self, name):
        self.name = name
        self._routes = {}

    def route(self, path, methods=None):
        methods = tuple((methods or ['GET']))
        def decorator(func):
            self._routes[(path, methods)] = func
            return func
        return decorator

    def test_client(self):
        app = self
        class Client:
            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc, tb):
                return False

            def get(self, path):
                func = app._routes.get((path, ('GET',)))
                if not func:
                    return Response({'error': 'not found'})
                global request
                request._data = {}
                return Response(func())

            def post(self, path, json=None):
                func = app._routes.get((path, ('POST',)))
                if not func:
                    return Response({'error': 'not found'})
                global request
                request._data = json or {}
                return Response(func())
        return Client()

    def run(self, host="127.0.0.1", port=5000):
        """Very small HTTP server for development."""
        from wsgiref.simple_server import make_server
        import json as _json

        def app_fn(environ, start_response):
            path = environ.get("PATH_INFO", "/")
            method = environ.get("REQUEST_METHOD", "GET")
            func = self._routes.get((path, (method,)))
            if not func:
                start_response("404 NOT FOUND", [("Content-Type", "application/json")])
                return [b'{"error": "not found"}']

            length = int(environ.get("CONTENT_LENGTH", "0") or 0)
            body = environ["wsgi.input"].read(length).decode("utf-8") if length else ""
            global request
            request._data = _json.loads(body) if body else {}
            resp = func()
            if isinstance(resp, str):
                start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
                return [resp.encode("utf-8")]
            start_response("200 OK", [("Content-Type", "application/json")])
            return [_json.dumps(resp).encode("utf-8")]

        server = make_server(host, port, app_fn)
        print(f"Serving on http://{host}:{port}")
        server.serve_forever()

request = Request()
