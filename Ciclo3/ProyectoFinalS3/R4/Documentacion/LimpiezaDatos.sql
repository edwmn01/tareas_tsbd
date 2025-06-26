use RendimientoAcademicoDB;
SET SQL_SAFE_UPDATES = 0;

DELETE direccion_email
FROM direccion_email
JOIN (
    SELECT email, MIN(id_email) AS id_keep
    FROM direccion_email
    GROUP BY email
) AS to_keep
ON direccion_email.email = to_keep.email
WHERE direccion_email.id_email != to_keep.id_keep;


SELECT email, COUNT(*) AS cantidad
FROM direccion_email
GROUP BY email
HAVING COUNT(*) > 1;

SELECT * FROM RendimientoAcademicoDB.direccion_email order by email ASC;

ALTER TABLE servicios
MODIFY COLUMN nombre_servicio VARCHAR(100) NOT NULL;

DROP TABLE servicio_vivienda;
DROP TABLE servicios;

DELETE FROM vivienda;
ALTER TABLE vivienda AUTO_INCREMENT = 1;

ALTER TABLE vivienda
ADD COLUMN servicios_basicos VARCHAR(100) NOT NULL;

DELETE FROM propiedad_extra;
ALTER TABLE propiedad_extra AUTO_INCREMENT = 1;

DELETE FROM contacto_emergencia;
ALTER TABLE contacto_emergencia AUTO_INCREMENT = 1;

ALTER TABLE contacto_emergencia
MODIFY COLUMN telefono_contacto VARCHAR(10) NOT NULL;

drop table datos_salud;
drop table colegio;
drop table titulacion_colegio;
drop table ocupacion_estudiante;


drop table titulacion_colegio;
ALTER TABLE titulacion_colegio AUTO_INCREMENT = 1;