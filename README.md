# COMP6411-A1
Python assignment for COMP 6411- Summer 2020

This solution code for A1 of COMP 6411 has 3 parts:

data.txt: This is the sample text file from which the data is parsed. This consists of values in the format: name|age|address|phone#. Each of the values can have leading or trailing spaces accompanied with them or any of the values except name can be left blank as well. For instance: abc||300 Mary Lane|112-122-1222 is a valid entry. The name is the one field that cannot be left blank and if it is, the parser in the server would absolutely ignore the data.

server.py: A server code that loads the data from data.txt, parses the data appropriately along with listening and responding to client queries. The server is also in an infinite loop, so once server file is run, the only way to stop is to kill the process from the IDE that you might be using or from the command line. 

client.py: The client file that presents the the DB menu for the user to play around with, view the data parsed from the data.txt file, update, delete and add new customers. The client also stays in an infinite loop with menu option being prompted again but a provision to kill the process is given in the menu. All the look up functions are performed by searching from the name. 

Steps to run:
Run the server.py file from one command line (Stays in an infinite loop)
Initiate another terminal and run the client.py file and play around with the data. 

Important information: No manipulations are made on data.txt file directly by the end of the process and all the playing around happens with the a dictionary inside the server.py. To check the update status of any operation, the entire report can be viewed from the DB Menu presented in the client frequently. The assignment is added alongside this repository to refer for more details. 
