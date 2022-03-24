from socket import *
import threading
import time
port = 9999

try:
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('127.0.0.1', port))
    clientSock.settimeout(5)
    msg = 'test'
    clientSock.send(msg.encode('utf-8'))
    data = clientSock.recv(1024)
    print('받은 데이터 : ', data.decode('utf-8'))
    clientSock.close()
except timeout:
    print('시간초과 다시시도해주세요.')
except Exception as e:
    print(e)
    print('에러발생..')