# importar modulos de la biblioteca Flask.
from flask import Flask , render_template

# crear objetos de la clase Flask, dando __name__ como argumento.
app = Flask(__name__)

# escribir las rutas usando las funciones "decorator".
# ruta o 'URL' predefinida.
@app.route("/")
def home():

    name = "Javier" # escribe tu nombre
    age = "17" # escribe tu edad

    return render_template('index.html' , name = name , age = age)

# define la ruta a la página web de tu padre.
@app.route("/father")
def father():

    name = "Javier" # escribe tu nombre
    age = "57" # escribe tu edad

    return render_template('father.html' , name = name , age = age)

# define la ruta a la página web de tu madre.
@app.route("/mother")
def mother():

    name = "Mireya" # escribe tu nombre
    age = "48" # escribe tu edad

    return render_template('mother.html' , name = name , age = age)

# define la ruta a la página web de tus amigos.
@app.route("/friend")
def friend():

    name = "Julio" # escribe tu nombre
    age = "16" # escribe tu edad

    return render_template('friend.html' , name = name , age = age)

# agrega otras rutas, si tú quieres.




# ejecuta el archivo
if __name__  ==  '__main__':
    app.run(debug=True)
