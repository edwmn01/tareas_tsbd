use had_p1_streamlit_personas;

drop table persona;
create table persona(
	id_persona int primary key auto_increment,
    nombre varchar(100),
    apellido varchar(100),
    cedula varchar(10),
    edad int,
    correo varchar(200),
    estado_civil varchar(50),
    telefono varchar(10),
    direccion varchar(200),
    Genero varchar(50)
);