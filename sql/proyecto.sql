
-- Table: proyecto
CREATE TABLE "proyecto" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(60) NOT NULL, "fecha_inicio" date NOT NULL, "fecha_entrega" date NOT NULL, "estado" varchar(10) NOT NULL, "imagen_proyecto" varchar(100) NULL, "valor_proyecto" integer unsigned NOT NULL, "progreso" smallint NOT NULL, "cliente_id" integer NOT NULL REFERENCES "cliente" ("id"));
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (1, 'Iglearon', '2017-09-12', '2017-12-23', 'cancelado', '', 423423, 0, 1);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (2, 'IPIN', '2017-09-12', '2017-12-23', 'cancelado', '', 423423, 0, 1);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (3, 'Logo', '2017-09-12', '2018-01-23', 'iniciado', '', 34234, 30, 3);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (4, 'Pendon', '2017-09-12', '2018-09-28', 'terminado', '', 5345345, 100, 4);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (5, 'Pendon', '2017-09-12', '2018-09-28', 'incompleto', '', 200000, 75, 5);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (6, 'Pasa Calle', '2017-09-12', '2018-09-28', 'cancelado', '', 200000, 0, 3);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (8, 'Tarjetas', '2017-11-16', '2017-11-21', 'iniciado', '', 34234, 30, 2);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (13, 'Folletos', '2023-09-20', '2023-12-20', 'incompleto', '', 423423, 75, 1);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (14, 'Folletos UDC', '2023-09-20', '2023-12-20', 'incompleto', '', 423423, 75, 1);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (15, 'Amed', '2017-11-17', '2017-11-17', 'incompleto', '', 978879, 75, 3);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (17, 'Salmon', '2017-11-30', '2017-12-08', 'iniciado', '', 534535345, 30, 3);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (18, 'Salmon Design', '2017-11-30', '2017-12-12', 'iniciado', '', 534535345, 30, 3);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (19, 'Luis', '2017-11-18', '2017-11-23', 'terminado', '', 23434244, 100, 3);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (20, 'Luis Daniel', '2017-10-31', '2017-11-15', 'incompleto', '', 534553, 75, 2);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (21, 'Colegio Manos Creativas', '2017-11-19', '2018-11-29', 'cancelado', '', 45345345, 0, 1);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (22, 'Fundacion', '2017-11-19', '2017-12-01', 'incompleto', '', 43535345, 75, 4);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (23, 'Salvador', '2017-11-08', '2017-11-17', 'terminado', '', 6436, 100, 2);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (24, 'Ppee', '2017-11-08', '2017-11-17', 'terminado', '', 6436, 100, 2);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (25, 'Panela', '2017-11-04', '2017-11-15', 'incompleto', '', 5435435, 75, 3);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (26, 'Formatos', '2017-11-15', '2017-12-08', 'incompleto', '', 7898778897, 75, 5);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (27, 'Branding', '2017-11-19', '2017-12-09', 'iniciado', '', 43545, 30, 2);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (28, 'Aweiken', '2017-11-21', '2017-11-30', 'incompleto', '', 234234, 75, 4);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (29, 'Pruebas', '2017-11-21', '2017-11-24', 'incompleto', '', 154543, 75, 2);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (30, 'TDT', '2017-11-2', '2018-12-10', 'incompleto', '', 65464646, 75, 1);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (31, 'Kennet Eventos', '2017-11-21', '2017-11-14', 'incompleto', '', 342342342, 75, 8);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (32, 'Amistad', '2017-11-22', '2017-12-22', 'incompleto', '', 324234234, 75, 7);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (33, 'Racing  Calendar', '2017-11-22', '2017-11-26', 'iniciado', '', 43432423, 30, 1);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (34, 'Amantes al poo', '2017-11-01', '2017-11-10', 'incompleto', '', 34534534, 75, 5);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (35, 'Amor a Dios', '2017-11-09', '2017-12-01', 'terminado', '', 32424234, 100, 3);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (36, 'Web Dev', '2017-11-01', '2018-06-14', 'iniciado', '', 47574757457, 30, 7);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (37, 'Juego UDC', '2017-11-17', '2017-11-23', 'incompleto', '', 6436345, 75, 4);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (38, 'Colegio', '2017-11-02', '2017-11-17', 'incompleto', '', 435345345, 75, 2);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (39, 'Confra', '2017-11-18', '2017-12-07', 'incompleto', '', 4213123, 75, 6);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (40, 'Puntillas', '2017-11-30', '2018-01-05', 'incompleto', '', 453453, 75, 2);
INSERT INTO proyecto (id, nombre, fecha_inicio, fecha_entrega, estado, imagen_proyecto, valor_proyecto, progreso, cliente_id) VALUES (41, 'Clavos', '2017-12-07', '2017-12-22', 'terminado', '', 34234234, 100, 4);