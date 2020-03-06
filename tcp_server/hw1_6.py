# дз 1.6.2
import socket
import os
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    print('new connection:', addr)
    dip = os.fork()
    if dip == 0:
        while True:
            data = conn.recv(1024)
            if data:
                if (data == b'close'):
                    break
                print(data, addr)
                conn.send(data)
        print('closing connection:', addr)
        conn.close()
        sys.exit()
    else:
        print('closing connection:', addr)
        conn.close()
s.close()
# import sys
# print('i am here')
# sys.exit()
# print('hey!')
