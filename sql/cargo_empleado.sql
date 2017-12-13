-- Table: cargo_empleado
CREATE TABLE "cargo_empleado" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(60) NOT NULL UNIQUE);
INSERT INTO cargo_empleado (id, nombre) VALUES (1, 'Desarrollador Backend');
INSERT INTO cargo_empleado (id, nombre) VALUES (2, 'Desarrollador  Frontend');
INSERT INTO cargo_empleado (id, nombre) VALUES (3, 'Diseñador gráfico');
INSERT INTO cargo_empleado (id, nombre) VALUES (4, 'Communy Manager');
INSERT INTO cargo_empleado (id, nombre) VALUES (5, 'Experto en UX');
INSERT INTO cargo_empleado (id, nombre) VALUES (6, 'Lider de Desarrollo');
INSERT INTO cargo_empleado (id, nombre) VALUES (7, 'Lider de redes');
INSERT INTO cargo_empleado (id, nombre) VALUES (8, 'Lider de mantenimiento');
INSERT INTO cargo_empleado (id, nombre) VALUES (9, 'Lider de electronica');
INSERT INTO cargo_empleado (id, nombre) VALUES (10, 'Asistente');
INSERT INTO cargo_empleado (id, nombre) VALUES (11, 'Teacher');