from socket import *
import threading
import time

port = 9999
serverSock = socket(AF_INET, SOCK_STREAM)

serverSock.bind(('', port))
serverSock.listen()

clients = []
nicknames = []

# 서버가 받은 메시지를 클라이언트 전체에 보내기
def broadcast(message): 
    for client in clients: 
        client.send(message)


def handle(client): 
    while True: 
        try: 
            # 클라이언트로부터 타당한 메시지를 받았는지 확인 
            message = client.recv(1024) 
            
            # 브로드캐스트 함수 동작 
            broadcast(message) 
        except: 
            # 클라이언트가 나갔으면 알림 
            index = clients.index(client) 
            clients.remove(client) 
            client.close() 

            nickname = nicknames[index] 
            broadcast("{} left!\n".format(nickname).encode('utf-8')) 
            broadcast("{} people in this room!\n".format(len(nicknames)).encode('utf-8')) 
            nicknames.remove(nickname) 
            break

def receive(): 
    while True: 
        client, address = serverSock.accept() 
        print("Connected with {}".format(str(address))) 
        client.send('NICKNAME'.encode('utf-8')) 
        nickname = client.recv(1024).decode('utf-8') 
        nicknames.append(nickname) 
        clients.append(client) 
        print("Nickname is {}".format(nickname)) 
        broadcast("{} joined!\n".format(nickname).encode('utf-8')) 
        broadcast("{} people in this room!\n".format(len(nicknames)).encode('utf-8')) 
        client.send('Connected to server!'.encode('utf-8')) 
        thread = threading.Thread(target=handle, args=(client,)) 
        thread.start()

receive()