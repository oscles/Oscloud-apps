-- Table: cliente
CREATE TABLE "cliente" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(45) NOT NULL, "apellido" varchar(45) NOT NULL, "telefono" varchar(10) NOT NULL, "direccion" varchar(100) NOT NULL, "tipo" varchar(17) NOT NULL, "email" varchar(254) NOT NULL UNIQUE);
INSERT INTO cliente (id, nombre, apellido, telefono, direccion, tipo, email) VALUES (1, 'Jony', 'Vargas', '2321', 'Nazareno', 'juridica', 'j@gmail.com');
INSERT INTO cliente (id, nombre, apellido, telefono, direccion, tipo, email) VALUES (2, 'Osnaider', 'Miranda', '324234', 'Mandela', 'juridica', 'osna@gmail.com');
INSERT INTO cliente (id, nombre, apellido, telefono, direccion, tipo, email) VALUES (3, 'Claudia ', 'Meza', '23231', 'Mandela', 'natural', 'meza@hmail.com');
INSERT INTO cliente (id, nombre, apellido, telefono, direccion, tipo, email) VALUES (4, 'Ruth', 'Meza', '98908', 'Mandela', 'juridica', 'ruth@gmail.com');
INSERT INTO cliente (id, nombre, apellido, telefono, direccion, tipo, email) VALUES (5, 'Sandra', 'Caceres', '875435', 'Villa Hermosa', 'natural', 'sandra@gmail.com');
INSERT INTO cliente (id, nombre, apellido, telefono, direccion, tipo, email) VALUES (6, 'Adonais', 'Medrano', '48324998', 'Sierrita', 'natural', 'ado@gmail.com');
INSERT INTO cliente (id, nombre, apellido, telefono, direccion, tipo, email) VALUES (7, 'Amauri', 'Cabarcas', '55234235', 'Mandela', 'natural', 'au@gmail.com');
INSERT INTO cliente (id, nombre, apellido, telefono, direccion, tipo, email) VALUES (8, 'Kennet', 'Martinez', '2342342343', 'Zaragocilla', 'natural', 'kenent@gmail.com');
