#Create a program where you enter an NBA player's name and see if they are an 2019 NBA All Star starter.
from __future__ import print_function, unicode_literals
import time

with open("Eastern_Conference_All_Star_Starters_2019.txt") as f: #opening the following text file and assigning a variable with the read function
    east_allstars = f.read()

east_allstars = east_allstars.splitlines() #spiliting text into columns "up to down"

east_header = east_allstars[0] #the first line on the text starting from the top
giannis = east_allstars[1]
kawhi = east_allstars[2]
embiid = east_allstars[3]
kyrie = east_allstars[4]
kemba = east_allstars[5]

print() #creating an extra line
print("Presenting your 2019... \n{}".format(east_header.upper())) #Printing the following string, adding a new line and formating the following variable with the uppercase function attached
time.sleep(3) #using the time module to wait 3 seconds before continuing the script
print() #creating an extra line
print("{:^30}{:^30}{:^30}".format("Player Name", "Position", "NBA Team")) #formatting the following string using the center indent by 30 characters and associating with the following strings consecutively
print("-" * 90) #added 90 lines
print("{:^30}{:^30}{:^30}".format(giannis, "Forward", "Milwaukee Bucks"))
print("{:^30}{:^30}{:^30}".format(kawhi, "Forward", "Toronto Raptors"))
print("{:^30}{:^30}{:^30}".format(embiid, "Center", "Philadelphia 76ers"))
print("{:^30}{:^30}{:^30}".format(kyrie, "Guard", "Boston Celtics"))
print("{:^30}{:^30}{:^30}".format(kemba, "Guard", "Charlotte Hornets"))
print()

nba_player = raw_input("Please enter an NBA player's name   :   ")
print()
print("Checking to see if {} is an Eastern Conference All Star... ".format(nba_player))
print()

time.sleep(3)

if nba_player == giannis:
    print("Yes, he is an Easter Conference All Star.")
elif nba_player == kawhi:
    print("Yes, he is an Eastern Conference All Star.")
elif nba_player == embiid:
    print("Yes, he is an Eastern Conference All Star.")
elif nba_player == kyrie:
    print("Yes, he is an Eastern Conference All Star.")
elif nba_player == kemba:
    print("Yes, he is an Eastern Conference All Star.")
else:
    print("No, he is not an Eastern Conference All Star.")
print()

time.sleep(3)

with open("Western_Conference_All_Star_Starters.txt") as f:
    west_allstars = f.read()

west_allstars = west_allstars.splitlines()

print("Checking to see if {} is an Western Conference All Star...".format(nba_player))
print()

time.sleep(3)

if nba_player in west_allstars:
    print("Yes, he is a Western Conference All Star.\n" )
else:
    print("No, he is not a Western Conference All Star.")
    print()
