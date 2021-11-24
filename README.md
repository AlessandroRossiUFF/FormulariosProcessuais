https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-pt

https://jinja.palletsprojects.com/en/2.10.x/templates/#template-inheritance

https://getbootstrap.com/

https://www.digitalocean.com/community/tutorials/how-and-when-to-use-sqlite

########################
https://flask-ptbr.readthedocs.io/en/latest/

DROP TABLE IF EXISTS processos;

CREATE TABLE processos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente VARCHAR (60),
    codigo VARCHAR (60),
    valor FLOAT (6,2),
    andamento INTEGER,
    observacoes TEXT,
    inicio DATE,
    fim DATE,
    cpf VARCHAR (11)
);