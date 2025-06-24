DROP DATABASE IF EXISTS RendimientoAcademicoDB;
CREATE DATABASE RendimientoAcademicoDB;
USE RendimientoAcademicoDB;

CREATE TABLE pais (
    id_pais INT PRIMARY KEY auto_increment,
    nombre_pais VARCHAR(250) NOT NULL
);

CREATE TABLE provincia (
    id_provincia INT PRIMARY KEY auto_increment,
    nombre_provincia VARCHAR(250) NOT NULL,
    id_pais INT,
    FOREIGN KEY (id_pais) REFERENCES pais(id_pais)
);

CREATE TABLE ciudad (
    id_ciudad INT PRIMARY KEY auto_increment,
    nombre_ciudad VARCHAR(250) NOT NULL,
    id_provincia INT,
    FOREIGN KEY (id_provincia) REFERENCES provincia(id_provincia)
);

CREATE TABLE barrio (
    id_barrio INT PRIMARY KEY auto_increment,
    sector VARCHAR(250) NOT NULL,
    tipo_parroquia VARCHAR(7),
    id_ciudad INT,
    FOREIGN KEY (id_ciudad) REFERENCES ciudad(id_ciudad)
);

CREATE TABLE estudiante (
    id_estudiante INT PRIMARY KEY auto_increment,
    cedula_pasaporte VARCHAR(20) NOT NULL,
    nombres VARCHAR(150) NOT NULL,
    apellidos VARCHAR(150) NOT NULL,
    sexo VARCHAR(1) NOT NULL,
    direccion TEXT,
    genero VARCHAR(50) NOT NULL,
    estado_civil VARCHAR(25) NOT NULL,
    lugar_nacimiento TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    nro_hijos INT NOT NULL,
    etnia VARCHAR(250) NOT NULL,
    idioma_nativo VARCHAR(100),
    celular VARCHAR(10) NOT NULL,
    telefono VARCHAR(10) NOT NULL,
    id_barrio INT NOT NULL,
    FOREIGN KEY (id_barrio) REFERENCES barrio(id_barrio)
);

CREATE TABLE direccion_email (
    id_email INT PRIMARY KEY auto_increment,
    email VARCHAR(250) NOT NULL,
    id_estudiante INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);


CREATE TABLE vivienda (
    id_vivienda INT PRIMARY KEY auto_increment,
    condicion_vivienda VARCHAR(100) NOT NULL,
    tipo_vivienda VARCHAR(50) NOT NULL,
    estructura_vivienda VARCHAR(50) NOT NULL,
    id_estudiante INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);


CREATE TABLE servicios (
    id_servicio_basico INT PRIMARY KEY auto_increment,
    nombre_servicio VARCHAR(50) NOT NULL
);



CREATE TABLE otra_titulacion (
    id_otra_titulacion INT PRIMARY KEY auto_increment,
    nombre_carrera VARCHAR(250) NOT NULL,
    registro_titulo VARCHAR(50) NOT NULL,
    id_estudiante INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

CREATE TABLE carrera (
    id_carrera INT PRIMARY KEY auto_increment,
    nombre_carrera VARCHAR(250) NOT NULL
);

CREATE TABLE carrera_estudiante (
    id_periodo INT PRIMARY KEY auto_increment,
    periodo VARCHAR(7),
    ciclo VARCHAR(15),
    razon_estudio VARCHAR(100),
    razones_eleccion_carrera VARCHAR(100),
    id_carrera INT,
    id_estudiante INT,
    FOREIGN KEY (id_carrera) REFERENCES carrera(id_carrera),
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

CREATE TABLE estructura_familiar (
    id_familiar INT PRIMARY KEY auto_increment,
    familiares_conviven TEXT NOT NULL,
    familiares_aportan_economicamente TEXT,
    cabezas_familia TEXT,
    familiares_cubren_estudio TEXT,
    id_estudiante INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

CREATE TABLE ayuda_economicamente (
    id_ayuda INT PRIMARY KEY auto_increment,
    tipo_ayuda TEXT NOT NULL,
    id_estudiante INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

BORRAR =============================================================
CREATE TABLE ocupacion_estudiante ( # Recuperar antes de eliminar
    id_ocupacion INT PRIMARY KEY auto_increment,
    tipo_ocupacion VARCHAR(50),
    id_estudiante INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);
BORRAR =============================================================

CREATE TABLE propiedad_extra (
    id_propiedad INT PRIMARY KEY auto_increment,
    nro_propiedades INT NOT NULL,
    valor_propiedades FLOAT,
    nro_vehiculo INT NOT NULL,
    valor_vehiculos FLOAT,
    id_estudiante INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

CREATE TABLE contacto_emergencia (
    id_emergencia INT PRIMARY KEY auto_increment,
    nombre_contacto VARCHAR(200) NOT NULL,
    telefono_contacto VARCHAR(10) NOT NULL,
    id_estudiante INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

CREATE TABLE beca (
    id_beca INT PRIMARY KEY auto_increment,
    tipo_beca TEXT NOT NULL,
    id_estudiante INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

CREATE TABLE colegio (
    id_colegio INT PRIMARY KEY auto_increment,
    nombre_colegio VARCHAR(250) NOT NULL,
    tipo_colegio VARCHAR(20) NOT NULL
);

CREATE TABLE titulacion_colegio (
    id_titulacion INT PRIMARY KEY auto_increment,
    anio_titulacion INT NOT NULL,
    tipo_titulacion VARCHAR(250) NOT NULL,
    id_estudiante INT,
    id_colegio INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (id_colegio) REFERENCES colegio(id_colegio)
);

CREATE TABLE finanzas (
    id_finanza INT PRIMARY KEY auto_increment,
    ingreso_mensual_estudiante FLOAT,
    ingreso_mensual_conyuge FLOAT,
    ingreso_mensual_padre FLOAT,
    ingreso_mensual_madre FLOAT,
    ingreso_mensual_otros_familiares FLOAT,
    otros_ingreso FLOAT,
    gasto_mensual_vivienda FLOAT,
    gasto_mensual_alimentacion FLOAT,
    gasto_mensual_educacion FLOAT,
    gasto_mensual_transporte FLOAT,
    gasto_mensual_salud FLOAT,
    gasto_mensual_servicios_basicos FLOAT,
    gasto_mensual_vestuarios FLOAT,
    gasto_mensual_otros FLOAT,
    id_estudiante INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

CREATE TABLE datos_salud (
    id_salud INT PRIMARY KEY auto_increment,
    tipo_sangre VARCHAR(10),
    discapacidad VARCHAR(150) NOT NULL,
    tipo_discapacidad TEXT,
    porcentaje_discapacidad FLOAT,
    carnet_conadis VARCHAR(50) NOT NULL,
    enfermedad_cronica VARCHAR(50) NOT NULL,
    enfermedad_catastrofica VARCHAR(50) NOT NULL,
    vacuna_covid VARCHAR(20) NOT NULL,
    ultima_vacuna_covid VARCHAR(100) NOT NULL,
    tiempo_embarazo_semanas INT NOT NULL,
    discapacidad_multiple TEXT NOT NULL,
    otras_enfermedades TEXT NOT NULL,
    antecedentes_patologicos_familiares VARCHAR(200) NOT NULL,
    parentesco_problema_salud VARCHAR(100) NOT NULL,
    id_estudiante INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

CREATE TABLE servicio_vivienda (
    id_servicio_vivienda INT PRIMARY KEY auto_increment,
    id_servicio_basico INT,
    id_vivienda INT,
    FOREIGN KEY (id_servicio_basico) REFERENCES servicios(id_servicio_basico),
    FOREIGN KEY (id_vivienda) REFERENCES vivienda(id_vivienda)
);

CREATE TABLE Notas (
  id_nota INT PRIMARY KEY AUTO_INCREMENT,
  id_estudiante INT,
  id_periodo INT,
  asignatura VARCHAR(100),
  asistencia FLOAT,
  nota_final FLOAT,
  estado ENUM('APROBADO', 'REPROBADO', 'RETIRADO'),
  FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
  FOREIGN KEY (id_periodo) REFERENCES carrera_estudiante(id_periodo)
);
