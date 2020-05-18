import socket

HOST= '127.0.0.1'
PORT= 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        print("\n")
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
            name= input("Enter the name: ")
            request_message= selection + "_" + name
            s.sendall(request_message.encode())
            data= s.recv(1024)
            print("\n")
            print(data.decode())
            continue

        if selection== "2":
            name= input("Enter the name: ")
            age= input("Enter the age: ")
            address= input("Enter the address: ")
            phone= input("Enter the phone number: ")
            request_message= selection + "_" + name + "|" + age + "|" + address + "|" + phone
            s.sendall(request_message.encode())
            data = s.recv(1024)
            print("\n")
            print(data.decode())
            continue

        if selection== "3":
            name=input("Enter the customer name you want to delete: ")
            request_message=selection + "_" + name
            s.sendall(request_message.encode())
            data = s.recv(1024)
            print("\n")
            print(data.decode())
            continue

        if selection== "4":
            name= input("Enter the customer name: ")
            age= input("Enter the age: ")
            request_message= selection + "_" + name + "_" + age
            s.sendall(request_message.encode())
            data = s.recv(1024)
            print("\n")
            print(data.decode())
            continue

        if selection== "5":
            name= input("Enter the customer name: ")
            address= input("Enter the address: ")
            request_message= selection + "_" + name + "_" + address
            s.sendall(request_message.encode())
            data = s.recv(1024)
            print("\n")
            print(data.decode())
            continue

        if selection== "6":
            name = input("Enter the customer name: ")
            phone = input("Enter the phone number: ")
            request_message = selection + "_" + name + "_" + phone
            s.sendall(request_message.encode())
            data = s.recv(1024)
            print("\n")
            print(data.decode())
            continue

        if selection== "7":
            request_message= selection + "_"
            request_message= "%s%s" % (request_message, None)
            s.sendall(request_message.encode())
            data = s.recv(1024)
            print("\n")
            print(data.decode())
            continue

        if selection=="8":
            break;
        data= s.recv(1024)

