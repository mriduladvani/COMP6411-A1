import socket
HOST = '127.0.0.1'
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    dictionary={}
    file= open("data.txt", "r")
    for x in file:
        y= x.split("|", 1)
        temp= y[1].split("|")
        value=""
        count=0
        for i in temp:
            if i.strip()=="":
                value="%s%s" % (value, None) #replace any empty values with None
            value = value + i.strip() #remove any leading or trailing white-spaces
            if count<2:
                value= value+ "|"
            count+=1
        dictionary[y[0]] = value;
    print(dictionary)
    while True:
        s.listen()
        conn, addr = s.accept()

        with conn:
            while True:
                data=conn.recv(1024)
                selection= data.decode().split("-")[0]
                if selection=="1":
                    name= data.decode().split("-")[1]
                    if name in dictionary:
                        print(dictionary[name])
                        conn.sendall((name + " " + " ".join(dictionary[name].split("|"))).encode())
                #elif selection=="2":

                if not data:
                    break
