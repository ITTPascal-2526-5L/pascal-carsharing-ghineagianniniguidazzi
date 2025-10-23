from flask import Flask

# Crea un istanza della classe Flask
app = Flask(__name__) 

# Route sono gli indirizzi(percorsi) a cui si può acccedere ('/') sta per la root principale, la primaria
@app.route('/')

# Le funzioni in python si fanno usando il 'def' al posto di 'function'
def home():
    return 'Hello World'
# Questa è una route (statica)
@app.route('/about')

# Questa è una view
def about():
    return 'Questa è la route about'

# Esempio di route dinamica (dentro '<>' e dentro il parametro (): deve essere uguale) 
# se scrivo 'str:' davanti al parametro passato nel URL mi aspetto che tipo di input 
# mi aspetto (non è essenziale metterlo) {presuppongo che faccia la stessa cosa con 'int:'} 
# Aggiornamento dal futuro 'str:' non funzia
@app.route('/user/<username>')
def user(username):
    return f"User: {username}"

# (Main)
if __name__ == '__main__':
    app.run
