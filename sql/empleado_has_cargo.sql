
-- Table: empleado_has_cargo
CREATE TABLE "empleado_has_cargo" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "empleado_id" integer NOT NULL REFERENCES "empleado" ("user_ptr_id"), "cargoempleado_id" integer NOT NULL REFERENCES "cargo_empleado" ("id"));
INSERT INTO empleado_has_cargo (id, empleado_id, cargoempleado_id) VALUES (1, 4, 1);
INSERT INTO empleado_has_cargo (id, empleado_id, cargoempleado_id) VALUES (2, 4, 3);
INSERT INTO empleado_has_cargo (id, empleado_id, cargoempleado_id) VALUES (3, 5, 2);
INSERT INTO empleado_has_cargo (id, empleado_id, cargoempleado_id) VALUES (4, 5, 3);
INSERT INTO empleado_has_cargo (id, empleado_id, cargoempleado_id) VALUES (5, 7, 2);
INSERT INTO empleado_has_cargo (id, empleado_id, cargoempleado_id) VALUES (6, 8, 4);
INSERT INTO empleado_has_cargo (id, empleado_id, cargoempleado_id) VALUES (8, 10, 2);
INSERT INTO empleado_has_cargo (id, empleado_id, cargoempleado_id) VALUES (9, 10, 5);