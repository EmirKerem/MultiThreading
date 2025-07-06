import socket
import datetime
from random import randint,choice
import threading
from _thread import start_new_thread
import time

lock = threading.Lock()

def returnin(msg):
    msg = (str(msg)).lower()
    l1 = ["heads", "tails"]
    if "time" in msg:
        time.sleep(5)
        return datetime.datetime.now().strftime(" It's %H:%M:%S")
    elif "random" in msg and "number" in msg:
        time.sleep(10)
        return str(choice(range(1, 11)))
    elif "heads" in msg or "tails" in msg:
        time.sleep(15)
        ans = randint(0, 1)
        return l1[ans]
    else:
        ans = "Please use basic words"
        return ans


def handleClient(client,addr):
    while True:
        msg = client.recv(1024).decode().strip()
        if not msg:
            break

        ans = returnin(msg)
        client.send(ans.encode())

    client.close()

def main():
    host = "127.0.0.1"
    port = 2424
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(3)
    print("Server is listening now from port:",port,".")

    while True:
        client, addr = server.accept()
        lock.acquire()
        print("Accepted connection from ",addr)
        lock.release()

        start_new_thread(handleClient,(client,addr))

if __name__ == "__main__":
    main()
