import time
import json
from flask import Flask, render_template
from flask_socketio import SocketIO
from robinround import User, round_robin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
processes = []


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/adminpanel')
def admin_panal():
    return render_template("admin.html")


@socketio.on("touches")
def admin(data):


    data_dict = data["data"]
    print(data_dict)
    time_quantum=data_dict[0]['time_quantum']
    for i in data_dict:
        user_id = i['id']
        bust_time = i['bust_time']
        b_time = i['bust_time']
        arrival_time = i['arrival_time']

        my_instance = User(user_id, bust_time, b_time, arrival_time)
        processes.append(my_instance)

    rr = round_robin(processes, time_quantum)
    my_report = {"report": rr["report"], "average_wait_time": rr["average_wait_time"]}
    print(my_report)
    socketio.emit("jerry", my_report)


@socketio.on("connect")
def check_connection():
    socketio.emit("check_thou", {"data": "connected yup"})


if __name__ == '__main__':
    socketio.run(app, debug=True, host="localhost", port=8000)
