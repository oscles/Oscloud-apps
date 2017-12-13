-- Table: empleado_has_skill
CREATE TABLE "empleado_has_skill" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "anios_experiencia" smallint NOT NULL, "id_empleado_id" integer NOT NULL REFERENCES "empleado" ("user_ptr_id"), "id_skill_id" integer NOT NULL REFERENCES "skill" ("id"));
INSERT INTO empleado_has_skill (id, anios_experiencia, id_empleado_id, id_skill_id) VALUES (1, 5, 1, 1);
INSERT INTO empleado_has_skill (id, anios_experiencia, id_empleado_id, id_skill_id) VALUES (2, 6, 1, 3);
INSERT INTO empleado_has_skill (id, anios_experiencia, id_empleado_id, id_skill_id) VALUES (3, 3, 6, 5);
INSERT INTO empleado_has_skill (id, anios_experiencia, id_empleado_id, id_skill_id) VALUES (4, 3, 1, 4);
INSERT INTO empleado_has_skill (id, anios_experiencia, id_empleado_id, id_skill_id) VALUES (5, 5, 1, 6);
