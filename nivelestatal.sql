
CREATE TABLE reportes
(
    reportesid INT NOT NULL PRIMARY KEY AUTO_INCREMENT, -- primary key column
    descripcion NVARCHAR(255) NOT NULL
);


CREATE TABLE ciclista
(
    ciclistaid INT NOT NULL PRIMARY KEY AUTO_INCREMENT, -- primary key column
    nombreCiclista NVARCHAR(255) NOT NULL,
    direccion NVARCHAR(255),
    telefono NVARCHAR(255)
);


CREATE TABLE municipios
(
    municipiosid INT NOT NULL PRIMARY KEY AUTO_INCREMENT, -- primary key column
    nombreMunicipio NVARCHAR(255)
);


CREATE TABLE bicicleta
(
    bicicletaid INT NOT NULL PRIMARY KEY AUTO_INCREMENT, -- primary key column
    marcabici NVARCHAR(255),
    modelobici NVARCHAR(255),
    no_serie NVARCHAR(255),
    fotobici mediumblob,
    ciclistaid INT, --FOREIGN KEY
    reportesid INT, --FOREIGN KEy
    FOREIGN KEY (ciclistaid) REFERENCES ciclista(ciclistaid),
    FOREIGN KEY (reportesid) REFERENCES reportes(reportesid)
);
