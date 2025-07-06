import socket

serverAddress = ("127.0.0.1",2424)

while True:
        msg = input("Ask about...('Time','Random Number' or 'Heads and Tails') Press Q for Quit")
        if msg == 'Q':
            break

        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.sendto(msg.encode(), serverAddress)
        ans , temp = client.recvfrom(1024)
        print("Answer is",ans.decode(),".")

        client.close()