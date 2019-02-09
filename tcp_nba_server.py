import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()

    with open("Eastern_Conference_All_Star_Starters_2019.txt") as f:
        east_allstars = f.read()

    east_allstars = east_allstars.splitlines()

    print("Connection from NBA fan:"    + str(addr))
    while True:
        data = c.recv(1024)
        if not data:
            break
        print("From connected user:"    + str(data))
        if data in east_allstars:
            data = "Yes, he is an Eastern Conference All Star."
            print("Sending:" + str(data))
        else:
            data = "No, he is not an Eastern Conference All Star."
        print("Sending:"    + str(data))
        c.send(data)
    c.close()

if __name__ == '__main__':
    Main()
