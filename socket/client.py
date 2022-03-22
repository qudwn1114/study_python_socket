from socket import *
import threading

port = 9999

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port))
nickname = input("Choose your nickname: ")

def receive(): 
    while True: 
        try: 
            message = clientSock.recv(1024).decode('utf-8') 
            if message == 'NICKNAME': clientSock.send(nickname.encode('utf-8')) 
            else: print(message) 
        except: 
            print("An error occured!") 
            clientSock.close() 
            break
def send(): 
    while True: 
        message = '{}: {}'.format(nickname, input('')) 
        clientSock.send(message.encode('utf-8'))

# 멀티 클라이언트용 쓰레드 
receive_thread = threading.Thread(target=receive) 
receive_thread.start() 

# 메시지 보내기 
send_thread = threading.Thread(target=send) 
send_thread.start()