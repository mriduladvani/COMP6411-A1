import socket

HOST= '127.0.0.1'
PORT= 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        print("Python DB Menu")
        print("1. Find Customer")
        print("2. Add Customer")
        print("3. Delete Customer")
        print("4. Update Customer age")
        print("5. Update Customer address")
        print("6. Update Customer phone")
        print("7. Print Report")
        print("8. Exit")
        selection= input("Select: ")
        if selection== "1":
            name= input("Enter the name")
            request_message= selection + "-" + name
            s.sendall(request_message.encode())
            data= s.recv(1024)
            print(data.decode())
            continue
        if selection=="8":
            break;
        data= s.recv(1024)

