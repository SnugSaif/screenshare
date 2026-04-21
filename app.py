from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

latest_frame = None

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('frame')
def receive_frame(data):
    global latest_frame
    latest_frame = data
    socketio.emit('screen', data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=10000)

