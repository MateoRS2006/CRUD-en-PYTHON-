CREATE database bdsenati;
USE bdsenati;
CREATE TABLE alumnos(
	codigo int auto_increment primary key,
    nombre varchar(50) not null,
    apellido varchar(40) not null,
    dni char(8) unique not null,
    fecha varchar(50) not null
);

CREATE DATABASE base_datos;
USE base_datos;
CREATE TABLE login_datos(
	Id int primary key AUTO_INCREMENT,
	Users varchar(50) not null,
	Password varchar(50) not null
)