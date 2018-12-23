import socket


def find_free_port():
    s = socket.socket()
    s.bind(("", 0))  # Bind to a free port provided by the host.
    return s.getsockname()[1]  # Return the port number assigned.
