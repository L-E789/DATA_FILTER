create database db_datafilter;
use db_datafilter;

create table users
(
	id int primary key not null auto_increment,
	name char(100),
    surname char(100),
    email char(150) unique,
    password char(150),
    img text,
    activated boolean,
    code char(15),
    recovery_date datetime
);

create table environments
(
	id int primary key not null auto_increment,
    img text,
    name char(120),
    key_code char(10),
    creation_date date,
    created_by int,
    foreign key (created_by) references users(id)
);

create table bridge
(
	id int primary key not null auto_increment,
    id_user int,
    id_environments int,
    v_admin boolean,
    linking_date date,
    state boolean,
    foreign key (id_user) references users(id),
    foreign key (id_environments) references environments(id)
);



/* ------------------------------------------------- */
create table estado
(
	id int primary key not null auto_increment,
    estado int(1)
);
select * from users;
Create Table dispositivos
(
	id int primary key not null auto_increment,
    User int,
    FOREIGN KEY (User) REFERENCES users(id),
    Cliente Char(150),
    telefono char(13),
    Direccion Char(100),
    FechaIngreso date,
    Equipo Char(100),
    Modelo Char(100),
    serial Char(20),
    Marca Char(100),
    FCompra Date,
    Accesorios Text,
    EstadoProduc Text,
    Falla Text,
    Diagnostico Text,
    Solucion Text,
    abono int,
    valor int,
    estado int,
    FOREIGN KEY (estado) REFERENCES estado(id)
);

create table informe
(
	id int primary key not null auto_increment,
    usuario int,
    FOREIGN KEY (usuario) REFERENCES users(id),
    dispositivo int,
    FOREIGN KEY (dispositivo) REFERENCES dispositivos(id)
);

create table entorno 
(
    codigo char(5) primary key not null,
    usuario int,
    FOREIGN KEY (usuario) REFERENCES users(id),
    fecha datetime
    
);


create table entorno_trabajo
(
	id int primary key not null auto_increment,
    entorno char(5),
    FOREIGN KEY (entorno) REFERENCES entorno(codigo),
    colaborador int, 
    FOREIGN KEY (colaborador) REFERENCES users(id)
)




