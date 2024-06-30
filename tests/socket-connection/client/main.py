# client.py

import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connection established')

@sio.event
def message(data):
    print('Received from server:', data)

@sio.event
def disconnect():
    print('Disconnected from server')

def logout():
    sio.send('logout')

if __name__ == '__main__':
    sio.connect('http://localhost:12345')
    
    try:
        while True:
            message = input("Enter a message (type 'logout' to disconnect): ")
            if message == 'logout':
                logout()
                break
            sio.send(message)
    except KeyboardInterrupt:
        print("Interrupted. Logging out.")
        logout()
    
    sio.wait()
