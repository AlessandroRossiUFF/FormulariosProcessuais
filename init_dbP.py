import sqlite3

connection = sqlite3.connect('databaseProcessos.db')
#abrirá uma conexão a um arquivo de banco de dados chamado database.db

with open('tabelaProcessos.sql') as f: 
    connection.executescript(f.read())#executa várias instruções SQL de uma só vez que criarão a tabela posts

cur = connection.cursor()#Crie um objeto de cursor que permita que você utilize o método execute() dele para executar duas instruções SQL INSERT para adicionar duas postagens do blog em sua tabela posts

cur.execute("INSERT INTO processos (cliente, codigo, valor, andamento, observacoes, cpf, inicio, fim) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ('Alessandro Rossi', '09876543210', 1030.35, 2, 'Alessandro Rossi', '02', '60/06/2021', '30/06/2021')
            )

cur.execute("INSERT INTO processos (cliente, codigo, valor, andamento, observacoes, cpf, inicio, fim) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ('Alessandro Rossi', '09876543210', 1030.35, 2, 'Alessandro Rossi', '02', '30/06/2021', '30/06/2021')
            )

connection.commit()#Por fim, confirme as alterações
connection.close()# e feche a conexão.

#Salve e feche o arquivo e, depois, execute-o no terminal usando o comando python: