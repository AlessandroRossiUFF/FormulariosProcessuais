from flask import Flask, render_template, flash, request, redirect, url_for
from sql import get_db_connection, get_post, get_processo, get_db_connectionP
# python init_db.py para iniciar o o database.db 
import os
from werkzeug.utils import secure_filename
#from config import *

#Dw-Up
UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


web_site = Flask(__name__)
web_site.config['SECRET_KEY'] = 'your secret key'
web_site.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #adicionará uma configuração SECRET_KEY
 

@web_site.route('/')
def index():
    conn = get_db_connection()
    connP = get_db_connectionP()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    processos = connP.execute('SELECT * FROM processos').fetchall()
    connP.close()
    conn.close()
    return render_template('index.html', posts=posts, processos=processos) #processos=processos #posts=posts,

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@web_site.route('/f', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(web_site.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@web_site.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@web_site.route('/<int:id>/processo')
def processo(id):
    processo = get_processo(id)
    return render_template('processo.html', processo=processo)

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

@web_site.route('/registro', methods=('GET', 'POST'))
def registro():
    if request.method == 'POST':
        cliente = request.form['cliente']
        codigo = request.form['codigo']
        nascimento = request.form['nascimento']
        observacoes = request.form['observacoes']
        inicio = request.form['inicio']
        prazo = request.form['prazo']
        valor = request.form['valor']

        if not codigo:
            flash('Preencha o código!')
        else:
            conn = get_db_connectionP()
            conn.execute('INSERT INTO processos (cliente, codigo, cpf, observacoes, inicio, fim, valor) VALUES (?, ?, ?, ?, ?, ?, ?)', (cliente, codigo, nascimento, observacoes, inicio, prazo, valor))                     
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('registro.html')


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

@web_site.route('/<int:id>/editar', methods=('GET', 'POST'))
def editar(id):
    post = get_processo(id)

    if request.method == 'POST':
        title = request.form['codigo']
        content = request.form['content']

        if not title:
            flash('Conteudo required!')
        else:
            conn = get_db_connectionP()
            conn.execute('UPDATE processos SET codigo = ?, observacoes = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('editar.html', post=post)
    post = get_processo(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Conteudo required!')
        else:
            conn = get_db_connectionP()
            conn.execute('UPDATE processos SET codigo = ?, observacoes = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('editar.html', post=post)


@web_site.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))
 
@web_site.route('/<int:id>/excluir', methods=('POST',))
def excluir(id):
    post = get_processo(id)
    conn = get_db_connectionP()
    conn.execute('DELETE FROM processos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))