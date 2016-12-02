import socket


def is_connected():
    REMOTE_SERVER = "www.google.com"
    try:
        print("Connecting.......")
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

