from socket import *

port = 8080

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port))

print('연결 확인 됐습니다.')

while True:
    recvData = clientSock.recv(1024)
    print('받은 데이터 : ', recvData.decode('utf-8'))

    sendData = input('>>>')
    clientSock.send(sendData.encode('utf-8'))
