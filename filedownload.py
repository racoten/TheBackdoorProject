import socket
import os

def Download(conn, filename, cwd):
    if ':\\' in cwd:
        f = open(f'{cwd}\\' + filename, 'wb')
    else:
        f = open(f'{cwd}/' + filename, 'wb')
    while True:
        bits = conn.recv(1024)
        if bits.endswith('DONE'.encode()):
            f.write(bits[:-4]) # Write those last received bits without the word 'DONE' 
            f.close()
            print ('[+] Transfer completed ')
            break
        if 'File not found'.encode() in bits:
            print ('[-] Unable to find out the file')
            break
        f.write(bits)