import socketserver
import socket
import sqlite3
import struct

def get_municipio_nombre(municipios_id, db_connection):
    return db_connection.execute('SELECT nombre_municipio FROM municipios WHERE municipios_id = ?', (municipios_id,)).fetchone()[0]

def get_ciclista_nombre(ciclista_id, db_connection):
    return db_connection.execute('SELECT nombre_ciclista FROM ciclista WHERE ciclista_id = ?', (ciclista_id,)).fetchone()[0]

def get_ciclista_correo(ciclista_id, db_connection):
    return db_connection.execute('SELECT correociclista FROM ciclista WHERE ciclista_id = ?', (ciclista_id,)).fetchone()[0]

def get_bicileta_marca(bicicleta_id, db_connection):
    return db_connection.execute('SELECT marcabici FROM bicicleta WHERE bicicleta_id = ?', (bicicleta_id,)).fetchone()[0]



class StateServerRequestHandler(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)
    
    def setup(self):
        return socketserver.BaseRequestHandler.setup(self)
    
    def handle(self):
        token = self.request.recv(1024)
        estado_id, municipio_id, ciclista_id, bicicleta_id = struct.unpack('>BIII', token)
        if estado_id == 255:
            self.server.finish = True
            return
            
        municipio = get_municipio_nombre(municipio_id, self.server.db_connection)
        ciclista = get_ciclista_nombre(ciclista_id, self.server.db_connection)
        correo = get_ciclista_correo(ciclista_id, self.server.db_connection)
        marca = get_bicileta_marca(bicicleta_id, self.server.db_connection)

        print("NOMBRE: {}\nMUNICIPIO: {}\nMARCA DE BICILETA: {}\nCORREO: {}".format(ciclista, municipio, marca, correo))

        
        

    def finish(self):
        return socketserver.BaseRequestHandler.finish(self)

class StateServer(socketserver.TCPServer):
    def __init__(self, server_address, database_file, handler_class=StateServerRequestHandler):
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


DATABASE_FILE = 'estatal.db'
DATABASE_SCHEMA = '../../sql/nivelestatal.sql'

def init_database(database_file, database_schema):
    conn = sqlite3.connect(database_file)
    with open(database_schema, "r") as schema_f:
        conn.executescript(schema_f.read())
    conn.close()

if __name__ == "__main__":

    init_database(DATABASE_FILE, DATABASE_SCHEMA)

    address = ('localhost', 8081)
    server = StateServer(address, DATABASE_FILE)

    server.serve_forever()