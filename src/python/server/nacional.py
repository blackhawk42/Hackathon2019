import socketserver
import sqlite3

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
    def __init__(self, server_address, database_file, handler_class=NationalServerRequestHandler):
        socketserver.TCPServer.__init__(self, server_address, handler_class)
        self.db_connection = sqlite3.connect(database_file)
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


DATABASE_FILE = 'nacional.db'
DATABASE_SCHEMA = '../../sql/nivelnacional.sql'

def init_database(database_file, database_schema):
    conn = sqlite3.connect(database_file)
    with open(database_schema, "r") as schema_f:
        conn.executescript(schema_f.read())
    conn.close()

if __name__ == "__main__":

    init_database(DATABASE_FILE, DATABASE_SCHEMA)

    address = ('localhost', 8080)
    server = NationalServer(address, DATABASE_FILE)

    server.serve_forever()