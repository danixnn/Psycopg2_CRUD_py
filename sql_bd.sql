-- Database: py_crud_simples

-- DROP DATABASE py_crud_simples;

CREATE DATABASE py_crud_simples
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
	
create table usuario(
	id serial primary key,
	nome varchar(20) not null,
	idade integer not null
);

insert into usuario(nome, idade)
values('Teste', 100);

select * from usuario;