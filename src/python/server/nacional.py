import socketserver

class NationalServerRequestHandler(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)
    
    def setup(self):
        return socketserver.BaseRequestHandler.setup(self)
    
    def handle(self):
        pass

    def finish(self):
        return socketserver.BaseRequestHandler.finish(self)

class NationalServer(socketserver.TCPServer):
    def __init__(self, server_address, handler_class=NationalServerRequestHandler):
        socketserver.TCPServer.__init__(self, server_address, handler_class)
        return
    
    def server_activate(self):
        socketserver.TCPServer.server_activate(self)
        return
    
    def serve_forever(self):
        while True:
            self.handle_request()

        return
    
    def handle_request(self):
        return socketserver.TCPServer.handle_request(self)

    def verify_request(self, request, client_address):
        return socketserver.TCPServer.verify_request(self, request, client_address)

    def process_request(self, request, client_address):
        return socketserver.TCPServer.process_request(self, request, client_address)

    def server_close(self):
        return socketserver.TCPServer.server_close(self)

    def finish_request(self, request, client_address):
        return socketserver.TCPServer.finish_request(self, request, client_address)

    def close_request(self, request_address):
        return socketserver.TCPServer.close_request(self, request_address)
