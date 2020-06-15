drop schema if exists ejercicio3;
create schema if not exists ejercicio3 char set utf8 collate utf8_spanish2_ci;

use ejercicio3;

create table empresa(
id bigint primary key auto_increment,
nombre varchar(255),
direccion text,
rfc varchar(255) unique
);

create table cliente(
id bigint primary key auto_increment,
empresa bigint,
nombre varchar(255),
direccion text,
rfc varchar(255) unique,
foreign key (empresa) references empresa(id)
);

create table producto(
id bigint primary key auto_increment,
nombre varchar(255),
precio_base double(10,2)
);

create table compra(
id bigint primary key auto_increment,
cliente bigint,
fecha_hora timestamp,
foreign key (cliente) references cliente(id)
);

create table detalle_compra(
id bigint primary key auto_increment,
compra bigint,
producto bigint,
precio_base double(10,2),
impuesto double(2,2),
descuento double(2,2),
cantidad bigint,
precio_final double(10,2),
foreign key (compra) references compra(id),
foreign key (producto) references producto(id)
);