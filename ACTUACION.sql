create database tia;
show databases;
use tia;
CREATE TABLE usuario(
  ci_usu varchar(10) NOT NULL,
  nombre_usu varchar(50) NOT NULL,
  apellido_usu varchar(50) NOT NULL,
  estado_civil_usu varchar(11) NOT NULL constraint ctrl_estado_civil_usu check (estado_civil_usu in ('casado','soltero','viudo','union libre')),
  sexo_usu char(9) NOT NULL constraint ctrl_tia_usu check (sexo_usu in ('Femenino','Masculino')), 
  direccion_usu varchar(50) NOT NULL,
  email_usu varchar(50) NOT NULL,
  telefono__usu varchar(10) NOT NULL,
  PRIMARY KEY (ci_usu)
) engine = innodb;


CREATE TABLE ventas(
  id_vent tinyint NOT NULL,
  nombre_vent varchar(50) NOT NULL,
  apellido_vent varchar(50) NOT NULL,
  direccion_vent varchar(50) NOT NULL,
  email_vent varchar(50) NOT NULL,
  celular_vent varchar(10) NOT NULL,
  precio_dist_vent decimal(6,2) NOT NULL constraint precio_dist_vent check (precio_dist_vent >= 0 and precio_dist_vent <=10), 
  precio_venta_vent decimal(6,2) NOT NULL, constraint precio_venta_vent check (precio_venta_vent > 10 and precio_venta_vent <= 100),
  PRIMARY KEY (id_vent)
) engine = innodb;

insert into usuario values('2200283790', "Eilyn", "Barragan", "union libre", "femenino", "coca", "barraganeilyn21@gmail.com", "0980643482");
insert into usuario values('2250160161', "jahir", "Zambrano", "soltero", "masculino", "coca", "jaoloor55@gmail.com", "0993837874");
insert into usuario values('2200418438', "Diana", "Ruiz", "viudo", "femenino", "coca", "janeth23@gmail.com", "0997543838");
insert into usuario values('2200481923', "Nhaily", "Barahona", "casado", "femenino", "coca", "barahonaNhaily@gmail.com", "0979711188");
insert into usuario values('2200435422', "Diego", "Ramirez", "viudo", "masculino", "coca", "ramirezdiego3@gmail.com", "0980331433");

insert into ventas values(1,"Nhaily", "Barahona", "coca", "barahonaNhaily@gmail.com", "0979711188", 5.25, 52.50);
insert into ventas values(2,"Jose", "Barahona", "coca", "barahonajose@gmail.com", "0989563456", 7.50, 99.50);
insert into ventas values(3,"Juan", "Guzman", "Quito", "juan123@gmail.com", "0956453424", 9.50, 100);
insert into ventas values(4,"Sofia", "Solorzano", "Guayaquil", "solorzanog43@mail.com", "0979342134", 3.50, 85);
insert into ventas values(5,"Darwil", "Esmeraldas", "Sacha", "esmeraldadarwil34@mail.com", "0979342134", 3.50, 85);

select * from usuario;
select * from ventas;

create view vista1_usuario as 
select ci_usu as cedula, nombre_usu as nombres, apellido_usu as apellidos from usuario;
select * from vista1_usuario;

create view vista1_ventas as 
select id_vent as Codigo, email_vent as Email, celular_vent as Celular from ventas;
select * from vista1_ventas;

create view vista2_ventas as 
select id_vent as Codigo, nombre_vent as Nombres, apellido_vent as Apellidos, precio_venta_vent as Precio_Venta from ventas
where precio_venta_vent>=50;

select * from vista2_ventas;

create view vista3_ventas as
select precio_dist_vent from ventas;
select SUM(precio_dist_vent) as Suma_Dist FROM ventas;

create view vista4_ventas as
select precio_venta_vent as Suma_vvista3_ventasvista4_ventasent from ventas;
select SUM(precio_venta_vent) as Suma_Vent FROM ventas;
