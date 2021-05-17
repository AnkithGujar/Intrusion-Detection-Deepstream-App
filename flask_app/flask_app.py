import cv2
import json
import time
import pandas as pd
import multiprocessing as mp
from datetime import datetime
from flask_socketio import emit, SocketIO
from flask import Flask, render_template, Response, request, url_for, redirect


app = Flask(__name__)


def bootstrap_on_connect():
    df = pd.read_csv('database.csv')
    emit('bootstrap', {'x': list(df.datetime), 'y1': list(df.entry_count_curr), 'y2': list(df.exit_count_curr), 'y3': list(df.boundary_count_curr)})

socketio = SocketIO(app, message_queue='redis://localhost:6379/')
socketio.on_event('connect', bootstrap_on_connect)


@app.route('/updateCount', methods = ['POST'])
def updateCount():

    global count_cum, x_list, y_list

    if request.method == 'POST':

        data = json.loads(request.data.decode())
        datetime_now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")

        socketio.emit('update', {'x': [datetime_now], 'y1': [data['entry_count_curr']], 'y2': [data['exit_count_curr']], 'y3': [data['boundary_count_curr']]})

        with open('database.csv', 'a') as f:
            f.write(datetime_now + ',' + str(data['entry_count_curr']) + ',' + str(data['exit_count_curr']) + ',' + str(data['boundary_count_curr']) + '\n')

    return 'success'


def gen_frames():
    global cap
    cap = cv2.VideoCapture('rtsp://localhost:8554/ds-test')
    # cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/live_streaming')
def liveStreaming():
    return render_template('live_streaming.html', x_window=100)


@app.route('/live_chart')
def liveChart():
    return render_template('live_chart.html', x_window=100)


@app.route('/both')
def both():
    return render_template('both.html')


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    socketio.run(app)