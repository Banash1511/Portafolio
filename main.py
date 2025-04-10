# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    if request.form.get('button_python'):
        return render_template('index.html', button_python=True)
    elif request.form.get('button_discord'):
        return render_template('index.html', button_discord=True)
    elif request.form.get('button_html'):
        return render_template('index.html', button_html=True)
    elif request.form.get('button_db'):
        return render_template('index.html', button_db=True)
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
