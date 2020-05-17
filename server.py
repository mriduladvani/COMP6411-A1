import socket
HOST = '127.0.0.1'
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    dictionary={}
    name= "John"
    file= open("data.txt", "r")
    for x in file:
        y= x.split("|", 1)
        dictionary[y[0]] = y[1];

    while True:
        s.listen()
        conn, addr = s.accept()




        with conn:
            while True:
                data=conn.recv(1024)
                if data.decode().split("-")[0]=="1":
                    name= data.decode().split("-")[1]
                    if name in dictionary:
                        conn.sendall((name + " " + " ".join(dictionary[name].split("|"))).encode())
                if not data:
                    break
