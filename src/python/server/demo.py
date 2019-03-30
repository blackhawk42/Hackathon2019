import socket
import struct
import sqlite3

SERVER = '127.0.0.1'
PORT = 8080

class Report:
    def __init__(self, report_id):
        self.report_id = report_id
    
    def __str__(self):
        as_bytes = struct.pack('>I', self.report_id)
        return '{} - {} - {} - {}'.format(as_bytes[0], as_bytes[1], as_bytes[2], as_bytes[3])
    

with sqlite3.connect("reportados.db") as db:
    with open('../../sql/reportados.sql') as schema_f:
        db.execute(schema_f.read())
        db.commit()

        cur = db.cursor()
        cur.execute('SELECT * FROM reportados')
        for row in cur:
            print("Encontre un reporte ID: {}".format(Report(row[0])))
            print("-> Notificando al nivel estatal")
            sock = socket.socket()
            sock.connect((SERVER, PORT))
            sock.sendall(b'3 ' + row[1])
            sock.close()
        cur.close()
    
