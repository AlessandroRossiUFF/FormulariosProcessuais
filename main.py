from blog import index, web_site, post, create, edit, delete
from users import user_loader, login, protected, logout, unauthorized_handler

#####################################
# WEB_SITE
web_site # web_site = Flask(__name__)

#####################################
# POSTAGENS
index # index.html

post # Posta as postagens

create # Cria as postagens

edit # Edita as postagens

delete # Deleta postagens

#####################################
#LOGIN 
user_loader # Carrega usuarios

login 

protected # Proteção 

logout

unauthorized_handler # Acesso negado
#####################################

web_site.run(host='0.0.0.0', port=8080)


