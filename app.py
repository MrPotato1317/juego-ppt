from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Ruta principal: Muestra el juego por primera vez
@app.route('/')
def index():
    return render_template('index.html')

# Ruta de juego: Procesa cuando haces clic en un botón
@app.route('/jugar', methods=['POST'])
def jugar():
    # Recibimos lo que el usuario eligió (el "value" del botón en HTML)
    usuario = request.form['eleccion']
    
    # La computadora elige al azar
    opciones = ['piedra', 'papel', 'tijera']
    computadora = random.choice(opciones)
    
    # Lógica de victoria
    if usuario == computadora:
        resultado = "¡Empate! 🤝"
    elif (usuario == 'piedra' and computadora == 'tijera') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijera' and computadora == 'papel'):
        resultado = "¡Ganaste! 🎉"
    else:
        resultado = "Perdiste... 😢"
    
    # Enviamos los datos de vuelta al HTML
    return render_template('index.html', 
                           resultado=resultado, 
                           pc=computadora, 
                           tu=usuario)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
