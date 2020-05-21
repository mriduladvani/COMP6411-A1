import socket
HOST = '127.0.0.1'
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    dictionary={}
    file= open("data.txt", "r")
    for x in file:
        y= x.split("|", 1)
        if y[0]=="":   #if the name is absent, the server skips that record.
            continue
        #next line makes sure that the age entered is a number, if it isnt, it skips the record
        if y[1].split("|", 1)[0].strip().isdigit()== False and y[1].split("|", 1)[0]!="":
            continue
        temp= y[1].split("|")
        value=""
        count=0
        for i in temp:
            if i.strip()=="":
                value="%s%s" % (value, None) #replace any empty values with None
            value = value + i.strip() #remove any leading or trailing white_spaces
            if count<2:
                value= value+ "|"
            count+=1
        dictionary[y[0].strip()] = value;
    print(dictionary)
    while True:
        s.listen()
        conn, addr = s.accept()

        with conn:
            while True:
                data=conn.recv(1024)
                selection= data.decode().split("_")[0]
                if selection=="1":
                    name= data.decode().split("_")[1]
                    if name in dictionary:
                        print(dictionary[name])
                        conn.sendall((name + " " + " ".join(dictionary[name].split("|"))).encode())
                    elif name not in dictionary:
                        conn.sendall(("Customer not found").encode())

                elif selection=="2":
                    record= data.decode().split("_")[1]
                    name= record.split("|", 1)[0].strip()
                    if name in dictionary:
                        conn.sendall(("Customer already exists").encode())
                    else:
                        if record.split("|")[1].isdigit()== True:
                            dictionary[name]= record.split("|", 1)[1]
                            conn.sendall(("Customer added").encode())
                        else:
                            conn.sendall(("Entered age is not a number").encode())
                    #print(dictionary)

                elif selection=="3":
                    #print(data.decode())
                    name = data.decode().split("_")[1]
                    if dictionary.pop(name, None) == None:
                        conn.sendall(("Customer does not exist").encode())
                    else:
                        conn.sendall(("Customer record deleted").encode())
                        print(dictionary)

                elif selection=="4":
                    name= data.decode().split("_")[1]
                    age= data.decode().split("_")[2] + "|"
                    if name not in dictionary:
                        conn.sendall(("Customer does not exist").encode())
                    else:
                        if data.decode().split("_")[2].isdigit()== True:
                            record=dictionary[name]
                            updated_record= age + record.split("|", 1)[1]
                            dictionary[name]=updated_record
                            print(dictionary)
                            conn.sendall(("Age update complete").encode())
                        else:
                            conn.sendall(("Entered age is not a number").encode())

                elif selection=="5":
                    name= data.decode().split("_")[1]
                    address= data.decode().split("_")[2]
                    if name not in dictionary:
                        conn.sendall(("Customer does not exist").encode())
                    else:
                        record=dictionary[name].split("|")
                        updated_record= record[0] + "|" + address + "|" + record[2]
                        dictionary[name]=updated_record
                        print(dictionary)
                        conn.sendall(("Age update complete").encode())

                elif selection=="6":
                    name= data.decode().split("_")[1]
                    phone= data.decode().split("_")[2]
                    if name not in dictionary:
                        conn.sendall(("Customer does not exist").encode())
                    else:
                        record=dictionary[name].split("|")
                        updated_record= record[0] + "|" +record[1] + "|"+ phone
                        dictionary[name]=updated_record
                        print(dictionary)
                        conn.sendall(("Phone number update complete").encode())

                elif selection=="7":
                    all_keys=""
                    report_3=""
                    report_1= "Name\t\tAge\t\tAddress\t\t\t\tPhone" + "\n..............................................................................\n"
                    print(report_1)
                    for x in dictionary:
                        all_keys+= x + " "
                    keys_list= all_keys.split(" ")
                    keys_list.sort()
                    keys_list.pop(0)
                    for x in keys_list:
                        record_list=[]
                        report_2=""
                        record_list=dictionary[x].split("|")
                        for y in range(len(record_list)):
                            report_2= report_2 + record_list[y] + "\t\t"
                        report_3= report_3 + x+"\t\t"+report_2+"\n"
                    #print(report_3)
                    conn.sendall((report_1 + report_3).encode())

                if not data:
                    break
