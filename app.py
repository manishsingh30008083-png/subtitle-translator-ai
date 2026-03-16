from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('translate')
def handle_translate(data):
    subtitle = data['subtitle']
    translated_subtitle = f"Translated: {subtitle}"
    time.sleep(1)  # Simulating delay
    emit('translation_response', {'translated': translated_subtitle})

if __name__ == '__main__':
    socketio.run(app, debug=True)