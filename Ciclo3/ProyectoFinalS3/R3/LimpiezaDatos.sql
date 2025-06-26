use RendimientoAcademicoDB;
SET SQL_SAFE_UPDATES = 0;

SELECT * FROM provincia order by nombre_provincia ASC;
SELECT * FROM ciudad order by nombre_ciudad ASC;
SELECT * FROM barrio order by sector ASC;

UPDATE ciudad
SET id_provincia = 1
WHERE nombre_ciudad = 'CUENCA';

UPDATE barrio
SET id_ciudad = 1
WHERE id_ciudad = 53;

DELETE FROM ciudad
WHERE id_ciudad = 53;

DELETE b1 FROM barrio b1
JOIN barrio b2 
  ON b1.sector = b2.sector
  AND b1.id_ciudad = b2.id_ciudad
  AND b1.id_barrio > b2.id_barrio;
