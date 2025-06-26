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




