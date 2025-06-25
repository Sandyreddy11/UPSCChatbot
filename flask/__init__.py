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

request = Request()
