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
def message(args):
    notification = Notify()
    notification.title = args['title']
    notification.message = args['message']
    notification.send()
    print('message', args['title'], args['message'])


def main():
    sio.connect('http://localhost:3000')
    sio.wait()

main()