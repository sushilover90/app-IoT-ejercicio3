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
nombre varchar(255),
direccion text,
rfc varchar(255) unique
);

create table producto(
id bigint primary key auto_increment,
nombre varchar(255),
precio_base double(10,2)
);

create table empresa_cliente(
id bigint primary key auto_increment,
empresa bigint,
cliente bigint,
 foreign key (empresa) references empresa(id),
 foreign key (cliente) references cliente(id)
);

create table compra(
id bigint primary key auto_increment,
empresa_cliente bigint,
fecha_hora timestamp,
foreign key (empresa_cliente) references empresa_cliente(id)
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

insert into empresa
(nombre,direccion,rfc)
values
('EMPRESA1','DIRECCION1','RFCEMPRESA1'),
('EMPRESA2','DIRECCION2','RFCEMPRESA2'),
('EMPRESA3','DIRECCION3','RFCEMPRESA3'),
('EMPRESA4','DIRECCION4','RFCEMPRESA4'),
('EMPRESA5','DIRECCION5','RFCEMPRESA5');

insert into cliente
(nombre,direccion,rfc)
values
('EDGAR','DIRECCIONEDGAR','RFCEDGAR'),
('FCO','DIRECCIONFCO','RFCFCO');

insert into empresa_cliente
(empresa,cliente)
values
(1,1),
(1,2);

select e.nombre,c.nombre from empresa_cliente ec join empresa e on ec.empresa = e.id join cliente c on ec.cliente = c.id;
