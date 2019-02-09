import socket
import time

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))
    time.sleep(3)
    print
    message = raw_input("Are you a commited NBA fan? How about we test your knowledge? \n Please enter an NBA player that has been selected as an Eastern Conference NBA All-Star starter this year:   \n ->")
    while message != 'q':
        s.send(message)
        data = s.recv(1024)
        print
        print("Checking with the NBA gods to see if you are correct...")
        print
        time.sleep(3)
        print("Here is the results: " + str(data))
        print
        time.sleep(3)
        message = raw_input("Enter another NBA player's name:   \n")
        time.sleep(3)
    else:
        print
        print("I hope you enjoyed this program, thank you.")
        s.close()

if __name__ == '__main__':
    Main()
