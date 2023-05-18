
CREATE DATABASE IF NOT EXISTS vistaViajes;
USE vistaViajes;


CREATE TABLE IF NOT EXISTS usuarios (
	usuarioID INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    contraseña VARCHAR(100) NOT NULL,
    correoRecuperacion VARCHAR(100) NOT NULL UNIQUE,
    celular VARCHAR(10),
    residencia VARCHAR(50)
); 

CREATE TABLE IF NOT EXISTS destinos (
	destinoID INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR (50) NOT NULL,
	descripcion VARCHAR (700) NOT NULL,
	imagen BLOB
);

CREATE TABLE IF NOT EXISTS viajes (
	viajeID INT PRIMARY KEY AUTO_INCREMENT,
    destinoID INT NOT NULL,
	nombreViaje VARCHAR(50) NOT NULL UNIQUE,
    descripcion VARCHAR(700) NOT NULL,
	fechaInicio TIMESTAMP NOT NULL,
	fechaFinal TIMESTAMP NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    cuposDisponibles INT NOT NULL,
    FOREIGN KEY (destinoID) REFERENCES destinos(destinoID)
);

CREATE TABLE IF NOT EXISTS reservas (
	reservaID INT PRIMARY KEY AUTO_INCREMENT,
    usuarioID INT NOT NULL,
    viajeID INT NOT NULL,
	FOREIGN KEY (usuarioID) REFERENCES usuarios(usuarioID),
	FOREIGN KEY (viajeID) REFERENCES viajes(viajeID),
    fecha TIMESTAMP NOT NULL,
    estado VARCHAR(20) NOT NULL
);

SHOW TABLES;

SELECT * FROM viajes;