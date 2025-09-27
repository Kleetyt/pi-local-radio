from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import os

app = Flask(__name__)

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "music")

# Ensure music folder exists
os.makedirs(BASE_DIR, exist_ok=True)

@app.route('/')
def index():
    stations = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))]
    return render_template('index.html', stations=stations)

@app.route('/station/<station_name>')
def station(station_name):
    station_folder = os.path.join(BASE_DIR, station_name)
    if not os.path.exists(station_folder):
        os.makedirs(station_folder)
    tracks = os.listdir(station_folder)
    return render_template('station.html', station=station_name, tracks=tracks)

@app.route('/upload/<station_name>', methods=['POST'])
def upload(station_name):
    if 'file' not in request.files:
        return redirect(url_for('station', station_name=station_name))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('station', station_name=station_name))
    station_folder = os.path.join(BASE_DIR, station_name)
    os.makedirs(station_folder, exist_ok=True)
    file.save(os.path.join(station_folder, file.filename))
    return redirect(url_for('station', station_name=station_name))

@app.route('/music/<station_name>/<filename>')
def music_file(station_name, filename):
    return send_from_directory(os.path.join(BASE_DIR, station_name), filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

