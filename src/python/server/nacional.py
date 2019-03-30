import socketserver
import sqlite3

def add_estado(nombre, direccion, db_connection):
    cur = db_connection.cursor()
    cur.execute('INSERT INTO estados(nombreestado, direccionestado) VALUES (?, ?)', (nombre, direccion))
    db_connection.commit()
    cur.close()

def remove_estado(estado_id, db_connection):
    cur = db_connection.cursor()
    cur.execute('DELETE FROM estados WHERE estado_id = ?', (estado_id,))
    db_connection.commit()
    cur.close()

def get_estado_direccion(estado_id, db_connection):
    return db_connection.execute('SELECT direccionestado FROM estados WHERE estado_id = ?', (estado_id,)).fetchone()[0]

class NationalServerRequestHandler(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)
    
    def setup(self):
        return socketserver.BaseRequestHandler.setup(self)
    
    def handle(self):
        data = self.request.recv(1024).decode('utf-8').split()
        data[0] = int(data[0])
        
        if data[0] == 1:
            try:
                add_estado(data[1], data[2], server.db_connection)
            except Exception as e:
                print(e)
        if data[0] == 2:
            remove_estado(data[1], server.db_connection)
        if data[0] == 3:
            print(get_estado_direccion(int(data[1]), server.db_connection))
        if data[0] == 4:
            server.finish = True

        
        

    def finish(self):
        return socketserver.BaseRequestHandler.finish(self)

class NationalServer(socketserver.TCPServer):
    def __init__(self, server_address, database_file, handler_class=NationalServerRequestHandler):
        socketserver.TCPServer.__init__(self, server_address, handler_class)
        self.db_connection = sqlite3.connect(database_file)
        self.finish = False
        return
    
    def server_activate(self):
        socketserver.TCPServer.server_activate(self)
        return
    
    def serve_forever(self):
        while not self.finish:
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