from flask import Flask, request, render_template 

web_site = Flask(__name__)

@web_site.route('/')
def hello():
    return 'Hello, World!'

@web_site.route('/soma')
def main():
    resultado = None
    media = None    

    primeira = request.args.get('primeira')
    segunda = request.args.get('segunda')

    if primeira and segunda:  
        primeira = float(primeira)
        segunda = float(segunda)

        media = (primeira + segunda) / 2
        if media >= 7:
            resultado = 'Aprovado'
        elif media >= 4:
            resultado = 'Recuperação'
        else:
            resultado = 'Reprovado'

    return render_template('index.html', media=media, resultado=resultado)

web_site.run(host='0.0.0.0', port=8080)