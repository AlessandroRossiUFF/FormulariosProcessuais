import sqlite3

connection = sqlite3.connect('database.db')
#abrirá uma conexão a um arquivo de banco de dados chamado database.db

with open('schema.sql') as f: 
    connection.executescript(f.read())#executa várias instruções SQL de uma só vez que criarão a tabela posts

cur = connection.cursor()#Crie um objeto de cursor que permita que você utilize o método execute() dele para executar duas instruções SQL INSERT para adicionar duas postagens do blog em sua tabela posts

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

connection.commit()#Por fim, confirme as alterações
connection.close()# e feche a conexão.

#Salve e feche o arquivo e, depois, execute-o no terminal usando o comando python: