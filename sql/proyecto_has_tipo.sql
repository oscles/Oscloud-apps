
-- Table: proyecto_has_tipo
CREATE TABLE "proyecto_has_tipo" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "proyecto_id" integer NOT NULL REFERENCES "proyecto" ("id"), "tipoproyecto_id" integer NOT NULL REFERENCES "tipo_proyecto" ("id"));
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (1, 31, 2);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (2, 31, 3);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (3, 31, 4);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (4, 31, 5);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (5, 32, 2);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (6, 32, 3);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (7, 32, 4);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (8, 33, 1);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (9, 34, 3);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (10, 35, 2);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (11, 36, 2);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (12, 36, 3);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (13, 36, 4);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (14, 36, 6);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (15, 37, 3);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (16, 38, 1);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (17, 38, 2);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (18, 38, 3);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (19, 38, 4);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (20, 39, 3);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (21, 40, 2);
INSERT INTO proyecto_has_tipo (id, proyecto_id, tipoproyecto_id) VALUES (22, 41, 6);
