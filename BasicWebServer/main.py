import socket
import sys
from _thread import *

host = '0.0.0.0'
port = 80

methods = ['GET', 'HEAD', 'POST', 'PUT','DELETE','CONNECT','OPTIONS','TRACE','PATCH']
versions = ['HTTP/1.1','HTTP/1.0','HTTP/2.0']
allow = ['html','json','jpg','png','js','css']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)
print('Waiting for a connection.')

def threaded_client(conn):
    while True:
        data = conn.recv(10000)


        #reply = 'Server output: ' + data.decode('utf-8')
        if not data:
            #conn.sendall(str.encode(reply))
            #conn.close()
            break
        data2 = data.decode('utf-8')
        head = data2.splitlines()

        if head[0].split(' ')[0] in methods and head[0].split(' ')[2] in versions:
            if head[0].split(' ')[1] == "/":
                filename = 'index.html'

            else:
                filename= head[0].split(' ')[1][1:]



            try:
                header=""
                if filename.endswith("html"):
                    header = "text/html"
                elif filename.endswith("css"):
                    header = "text/css"
                elif filename.endswith("png"):
                    header = "image/png"
                else:
                    reply = 'HTTP/1.1 404 Page not Found\n\n HATA3'
                    conn.sendall(str.encode(reply))
                    conn.close()
                    break

                with open(filename, 'rb') as f:
                    conn.send(str.encode('HTTP/1.1 200 OK\n' + 'Content-Type: ' + header + "\n\n"))
                    data = f.read()
                    print(data)
                    conn.send(data)
                conn.close()
                break

            except:
                reply = 'HTTP/1.1 404 Page not Found\n\n HATA1'
                conn.sendall(str.encode(reply))
                conn.close()
                exit_thread()
                break

        else:
            reply = 'HTTP/1.1 400 Bad Request\n'
            conn.sendall(str.encode(reply))
            conn.close()
            exit_thread()
            break
    conn.close()
    exit_thread()


while True:
    conn, addr = s.accept()
    print('connected to: ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(threaded_client, (conn,))
