from socket import *
import threading
import time

port = 9999
serverSock = socket(AF_INET, SOCK_STREAM)

serverSock.bind(('', port))
serverSock.listen()

clients = []

# 접속 클라이언트들 확인
def check(message): 
    for client in clients: 
        client.send(message)


def handle(client): 
    while True: 
        try: 
            message = 'check!'.encode('utf-8')
            check(message)
        except: 
            # 클라이언트가 나갔으면 제거
            clients.remove(client) 
            client.close()
            print('총인원', len(clients))
            break
        time.sleep(0.5)

def receive(): 
    while True: 
        client, address = serverSock.accept() 
        print("Connected with {}".format(str(address)))
        nickname = client.recv(1024).decode('utf-8') 
        clients.append(client) 
        print("Nickname is {}".format(nickname)) 
        client.send('Connected to server!'.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,)) 
        thread.start()

receive()