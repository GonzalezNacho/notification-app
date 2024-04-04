from notifypy import Notify
import socketio

sio = socketio.Client()

@sio.event
def on_connect():
    print('connect')

@sio.event
def disconnect():
    print('disconnected')


@sio.event
def message(*args):
    notification = Notify()
    notification.title = args[0]
    notification.message = args[1]
    notification.send()
    print('message', args[0], args[1])


def main():
    sio.connect('http://localhost:3000')
    sio.wait()

main()