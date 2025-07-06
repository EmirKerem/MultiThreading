import socket


while True:
        msg = input("Ask about...('Time','Random Number' or 'Heads and Tails') Press Q for Quit")
        if msg == 'Q':
            break

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 2424))


        client.send(msg.encode())
        ans = client.recv(1024).decode()
        print("Answer is : ", ans)

        client.close()