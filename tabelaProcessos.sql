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