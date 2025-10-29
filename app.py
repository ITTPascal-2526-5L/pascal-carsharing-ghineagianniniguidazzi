# Questo file serve solo per lanciare ò'istanza.
# L'istanza e le sue dipendenze (librerie) sono state settate all'interno del file __init__
from .app import create_app

app= create_app()

if __name__ == "__main__":
    app.run(debug=True)