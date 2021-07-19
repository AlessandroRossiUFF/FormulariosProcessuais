import sqlite3
from werkzeug.exceptions import abort

import flask_login 

login_manager = flask_login.LoginManager()

users = {'foo@bar.tld': {'password': 'secret'}}

####################################
# CONECT 
def get_db_connection():
    conn = sqlite3.connect('database.db')#abre uma conexão ao arquivo de banco de dados database.db
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    #create que aceita as solicitações GET e POST. As solicitações GET são aceitas por padrão. Para também aceitar as solicitações POST, que são enviadas pelo navegador ao enviar formulários, você passará uma tupla com os tipos de solicitações aceitos para o argumento methods do decorador @app.route().
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post
# CONECT 
####################################