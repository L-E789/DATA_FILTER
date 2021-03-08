create table DB_DataFilter;
use DB_DataFilter;

create table rango
(
	id int primary key not null auto_increment,
	tipo int(1)
);

create table users
(
	id int primary key not null auto_increment,
	nombre char(100),
    email char(150),
    password char(150),
    rango int,
	FOREIGN KEY (rango) REFERENCES rango(id)
);

create table estado
(
	id int primary key not null auto_increment,
    estado int(1)
);

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
	id int primary key not null auto_increment,
    usuario int,
    FOREIGN KEY (usuario) REFERENCES users(id),
    fecha date
);

create table colaborador
(
	id int primary key not null auto_increment,
    usuario int,
    FOREIGN KEY (usuario) REFERENCES users(id)
);


create table entorno_trabajo
(
	id int primary key not null auto_increment,
    entorno int,
    FOREIGN KEY (entorno) REFERENCES entorno(id),
    colaborador int, 
    FOREIGN KEY (colaborador) REFERENCES colaborador(id)
)




