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


def handleClient(msg,addr,server):
    msg = msg.decode().strip()
    ans = returnin(msg)
    server.sendto(ans.encode(), addr)

def main():
    host = "127.0.0.1"
    port = 2424
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))

    print("UDP Server Started on port",port,".")

    while True:
        msg, addr = server.recvfrom(1024)

        lock.acquire()
        print("Connected to :",addr)
        lock.release()

        start_new_thread(handleClient,(msg,addr,server))

if __name__ == "__main__":
    main()

