CREATE TABLE IF NOT EXISTS reportes
(
    reportes_id INTEGER PRIMARY KEY AUTOINCREMENT, -- primary key column
    descripcion TEXT
);


CREATE TABLE IF NOT EXISTS ciclista
(
    ciclista_id INTEGER PRIMARY KEY AUTOINCREMENT, -- primary key column
    nombre_ciclista TEXT NOT NULL,
    direccion TEXT,
    telefono TEXT,
    correociclista TEXT,
    contraseñaciclista TEXT
);


CREATE TABLE IF NOT EXISTS municipios
(
    municipios_id INTEGER PRIMARY KEY AUTOINCREMENT, -- primary key column
    nombre_municipio TEXT
);


CREATE TABLE IF NOT EXISTS bicicleta
(
    bicicleta_id INTEGER PRIMARY KEY AUTOINCREMENT, -- primary key column
    marcabici TEXT,
    modelobici TEXT,
    no_serie TEXT,
    fotobici mediumblob,
    ciclista_id INTEGER, --FOREIGN KEY
    reportes_id INTEGER, --FOREIGN KEy
    FOREIGN KEY (ciclista_id) REFERENCES ciclista(ciclista_id),
    FOREIGN KEY (reportes_id) REFERENCES reportes(reportes_id)
);
