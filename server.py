import socket
HOST = '127.0.0.1'
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) #bind the socket with network interface and port

    while True:
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected By:', addr)
            while True:
                data=conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)