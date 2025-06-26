DROP DATABASE IF EXISTS `RendimientoAcademicoDB`;
CREATE DATABASE  IF NOT EXISTS `RendimientoAcademicoDB`;
 
USE `RendimientoAcademicoDB`;


DROP TABLE IF EXISTS `ayuda_economicamente`;
CREATE TABLE `ayuda_economicamente` (
  `id_ayuda` int NOT NULL AUTO_INCREMENT,
  `tipo_ayuda` text NOT NULL,
  `id_estudiante` int DEFAULT NULL,
  PRIMARY KEY (`id_ayuda`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `ayuda_economicamente_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `barrio`;
CREATE TABLE `barrio` (
  `id_barrio` int NOT NULL AUTO_INCREMENT,
  `sector` varchar(250) NOT NULL,
  `tipo_parroquia` varchar(7) DEFAULT NULL,
  `id_ciudad` int DEFAULT NULL,
  PRIMARY KEY (`id_barrio`),
  KEY `id_ciudad` (`id_ciudad`),
  CONSTRAINT `barrio_ibfk_1` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudad` (`id_ciudad`)
) ENGINE=InnoDB AUTO_INCREMENT=2599 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `beca`;
CREATE TABLE `beca` (
  `id_beca` int NOT NULL AUTO_INCREMENT,
  `tipo_beca` text NOT NULL,
  `id_estudiante` int DEFAULT NULL,
  PRIMARY KEY (`id_beca`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `beca_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `carrera`;
CREATE TABLE `carrera` (
  `id_carrera` int NOT NULL AUTO_INCREMENT,
  `nombre_carrera` varchar(250) NOT NULL,
  PRIMARY KEY (`id_carrera`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `carrera_estudiante`;
CREATE TABLE `carrera_estudiante` (
  `id_periodo` int NOT NULL AUTO_INCREMENT,
  `periodo` varchar(7) DEFAULT NULL,
  `ciclo` varchar(15) DEFAULT NULL,
  `razon_estudio` varchar(100) DEFAULT NULL,
  `razones_eleccion_carrera` varchar(100) DEFAULT NULL,
  `id_carrera` int DEFAULT NULL,
  `id_estudiante` int DEFAULT NULL,
  PRIMARY KEY (`id_periodo`),
  KEY `id_carrera` (`id_carrera`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `carrera_estudiante_ibfk_1` FOREIGN KEY (`id_carrera`) REFERENCES `carrera` (`id_carrera`),
  CONSTRAINT `carrera_estudiante_ibfk_2` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=1446 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `ciudad`;
CREATE TABLE `ciudad` (
  `id_ciudad` int NOT NULL AUTO_INCREMENT,
  `nombre_ciudad` varchar(250) NOT NULL,
  `id_provincia` int DEFAULT NULL,
  PRIMARY KEY (`id_ciudad`),
  KEY `id_provincia` (`id_provincia`),
  CONSTRAINT `ciudad_ibfk_1` FOREIGN KEY (`id_provincia`) REFERENCES `provincia` (`id_provincia`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `contacto_emergencia`;
CREATE TABLE `contacto_emergencia` (
  `id_emergencia` int NOT NULL AUTO_INCREMENT,
  `nombre_contacto` varchar(200) NOT NULL,
  `telefono_contacto` varchar(10) NOT NULL,
  `id_estudiante` int DEFAULT NULL,
  PRIMARY KEY (`id_emergencia`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `contacto_emergencia_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=1224 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `datos_salud`;
CREATE TABLE `datos_salud` (
  `id_salud` int NOT NULL AUTO_INCREMENT,
  `tipo_sangre` varchar(10) DEFAULT NULL,
  `discapacidad` text NOT NULL,
  `porcentaje_discapacidad` float DEFAULT NULL,
  `carnet_conadis` varchar(50) NOT NULL,
  `enfermedad_cronica` text NOT NULL,
  `enfermedad_catastrofica` text NOT NULL,
  `ultima_vacuna_covid` varchar(100) NOT NULL,
  `tiempo_embarazo_semanas` int NOT NULL,
  `discapacidad_multiple` text NOT NULL,
  `otras_enfermedades` text NOT NULL,
  `antecedentes_patologicos_familiares` varchar(200) NOT NULL,
  `parentesco_problema_salud` varchar(100) NOT NULL,
  `id_estudiante` int DEFAULT NULL,
  PRIMARY KEY (`id_salud`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `datos_salud_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=1334 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `direccion_email`;
CREATE TABLE `direccion_email` (
  `id_email` int NOT NULL AUTO_INCREMENT,
  `email` varchar(250) NOT NULL,
  `id_estudiante` int DEFAULT NULL,
  PRIMARY KEY (`id_email`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `direccion_email_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=3480 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `estructura_familiar`;
CREATE TABLE `estructura_familiar` (
  `id_familiar` int NOT NULL AUTO_INCREMENT,
  `familiares_conviven` text NOT NULL,
  `familiares_aportan_economicamente` text,
  `cabezas_familia` text,
  `familiares_cubren_estudio` text,
  `id_estudiante` int DEFAULT NULL,
  PRIMARY KEY (`id_familiar`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `estructura_familiar_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=1295 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `estudiante`;
CREATE TABLE `estudiante` (
  `id_estudiante` int NOT NULL AUTO_INCREMENT,
  `cedula_pasaporte` varchar(20) NOT NULL,
  `nombres` varchar(150) NOT NULL,
  `apellidos` varchar(150) NOT NULL,
  `sexo` varchar(1) NOT NULL,
  `direccion` text,
  `genero` varchar(50) NOT NULL,
  `estado_civil` varchar(25) NOT NULL,
  `lugar_nacimiento` text NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `nro_hijos` int NOT NULL,
  `etnia` varchar(250) NOT NULL,
  `idioma_nativo` varchar(100) DEFAULT NULL,
  `celular` varchar(10) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `id_barrio` int NOT NULL,
  PRIMARY KEY (`id_estudiante`),
  KEY `id_barrio` (`id_barrio`),
  CONSTRAINT `estudiante_ibfk_1` FOREIGN KEY (`id_barrio`) REFERENCES `barrio` (`id_barrio`)
) ENGINE=InnoDB AUTO_INCREMENT=981 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `finanzas`;
CREATE TABLE `finanzas` (
  `id_finanza` int NOT NULL AUTO_INCREMENT,
  `ingreso_mensual_estudiante` float DEFAULT NULL,
  `ingreso_mensual_conyuge` float DEFAULT NULL,
  `ingreso_mensual_padre` float DEFAULT NULL,
  `ingreso_mensual_madre` float DEFAULT NULL,
  `ingreso_mensual_otros_familiares` float DEFAULT NULL,
  `otros_ingreso` float DEFAULT NULL,
  `gasto_mensual_vivienda` float DEFAULT NULL,
  `gasto_mensual_alimentacion` float DEFAULT NULL,
  `gasto_mensual_educacion` float DEFAULT NULL,
  `gasto_mensual_transporte` float DEFAULT NULL,
  `gasto_mensual_salud` float DEFAULT NULL,
  `gasto_mensual_servicios_basicos` float DEFAULT NULL,
  `gasto_mensual_vestuarios` float DEFAULT NULL,
  `gasto_mensual_otros` float DEFAULT NULL,
  `id_estudiante` int DEFAULT NULL,
  PRIMARY KEY (`id_finanza`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `finanzas_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=1401 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



DROP TABLE IF EXISTS `ocupacion_estudiante`;
CREATE TABLE `ocupacion_estudiante` (
  `id_ocupacion` int NOT NULL AUTO_INCREMENT,
  `tipo_ocupacion` varchar(50) DEFAULT NULL,
  `id_estudiante` int DEFAULT NULL,
  PRIMARY KEY (`id_ocupacion`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `ocupacion_estudiante_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=1033 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `otra_titulacion`;
CREATE TABLE `otra_titulacion` (
  `id_otra_titulacion` int NOT NULL AUTO_INCREMENT,
  `nombre_carrera` varchar(250) NOT NULL,
  `registro_titulo` varchar(50) NOT NULL,
  `id_estudiante` int DEFAULT NULL,
  PRIMARY KEY (`id_otra_titulacion`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `otra_titulacion_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=134 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `pais`;
CREATE TABLE `pais` (
  `id_pais` int NOT NULL AUTO_INCREMENT,
  `nombre_pais` varchar(250) NOT NULL,
  PRIMARY KEY (`id_pais`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `propiedad_extra`;
CREATE TABLE `propiedad_extra` (
  `id_propiedad` int NOT NULL AUTO_INCREMENT,
  `nro_propiedades` int NOT NULL,
  `valor_propiedades` float DEFAULT NULL,
  `nro_vehiculo` int NOT NULL,
  `valor_vehiculos` float DEFAULT NULL,
  `id_estudiante` int DEFAULT NULL,
  PRIMARY KEY (`id_propiedad`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `propiedad_extra_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=1111 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `provincia`;
CREATE TABLE `provincia` (
  `id_provincia` int NOT NULL AUTO_INCREMENT,
  `nombre_provincia` varchar(250) NOT NULL,
  `id_pais` int DEFAULT NULL,
  PRIMARY KEY (`id_provincia`),
  KEY `id_pais` (`id_pais`),
  CONSTRAINT `provincia_ibfk_1` FOREIGN KEY (`id_pais`) REFERENCES `pais` (`id_pais`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `titulacion_colegio`;
CREATE TABLE `titulacion_colegio` (
  `id_titulacion` int NOT NULL AUTO_INCREMENT,
  `nombre_colegio` text NOT NULL,
  `tipo_colegio` varchar(20) NOT NULL,
  `anio_titulacion` int NOT NULL,
  `tipo_titulacion` varchar(250) NOT NULL,
  `id_estudiante` int DEFAULT NULL,
  PRIMARY KEY (`id_titulacion`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `titulacion_colegio_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=1365 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `vivienda`;
CREATE TABLE `vivienda` (
  `id_vivienda` int NOT NULL AUTO_INCREMENT,
  `condicion_vivienda` varchar(100) NOT NULL,
  `tipo_vivienda` varchar(50) NOT NULL,
  `estructura_vivienda` varchar(50) NOT NULL,
  `id_estudiante` int DEFAULT NULL,
  `servicios_basicos` varchar(100) NOT NULL,
  PRIMARY KEY (`id_vivienda`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `vivienda_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=1246 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
