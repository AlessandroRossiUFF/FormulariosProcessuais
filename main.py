import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
  #A função flash() armazena mensagens flash na sessão do navegador do cliente.
from werkzeug.exceptions import abort
import  flask_login 
import flask
login_manager = flask_login.LoginManager()

# Our mock database.
users = {'foo@bar.tld': {'password': 'secret'}}

############################
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
############################

web_site = Flask(__name__)
web_site.config['SECRET_KEY'] = 'your secret key' #adicionará uma configuração SECRET_KEY ao seu aplicativo através do objeto app.config. Lembre-se de que a chave secreta deve ser uma string aleatória longa.

@web_site.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index2.html', posts=posts)

@web_site.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

#Após definir uma chave secreta, você criará uma função que renderizará um modelo que mostra um formulário onde é possível criar uma nova postagem do blog.
@web_site.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@web_site.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@web_site.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

##############################
#LOGIN LOGIN LOGIN LOGIN LOGIN 
class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user


@web_site.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = flask.request.form['email']
    if flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    return 'Bad login'

@web_site.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@web_site.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'
#LOGIN LOGIN LOGIN LOGIN LOGIN 
##############################

login_manager.init_app(web_site)
web_site.run(host='0.0.0.0', port=8080)


