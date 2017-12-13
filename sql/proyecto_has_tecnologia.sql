
-- Table: proyecto_has_tecnologia
CREATE TABLE "proyecto_has_tecnologia" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "proyecto_id" integer NOT NULL REFERENCES "proyecto" ("id"), "tecnologia_id" integer NOT NULL REFERENCES "tecnologia" ("id"));
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (1, 31, 1);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (2, 31, 2);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (3, 31, 3);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (4, 31, 5);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (5, 31, 6);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (6, 32, 2);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (7, 32, 4);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (8, 32, 5);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (9, 33, 6);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (10, 34, 4);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (11, 34, 5);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (12, 35, 5);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (13, 36, 2);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (14, 36, 3);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (15, 36, 4);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (16, 36, 5);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (17, 36, 6);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (18, 37, 4);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (19, 37, 6);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (20, 38, 5);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (21, 38, 6);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (22, 39, 4);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (23, 40, 6);
INSERT INTO proyecto_has_tecnologia (id, proyecto_id, tecnologia_id) VALUES (24, 41, 1);
