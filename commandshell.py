import socket

def shell(connection, CWD):
    while True:
        command = input(f"{CWD}$ ")
        if command == 'exit':
            connection.send('exit'.encode())
            break
        elif 'cd' in command:
            cmd_path = 'cd ' + command.split(" ")[1]
            connection.send(cmd_path.encode())
        elif command == 'pwd':
            connection.send('pwd'.encode())
        connection.send(command.encode())
        print(connection.recv(4096).decode())
