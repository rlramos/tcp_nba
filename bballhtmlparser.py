from __future__ import unicode_literals, absolute_import, print_function, division
import requests
from bs4 import BeautifulSoup
from pprint import pprint

def printBoard(values):
    print("{:^15}{:^15}{:^15}".format(*values[:3]))
    print("{:^15}{:^15}{:^15}".format(*values[3:6]))
    print("{:^15}{:^15}{:^15}".format(*values[6:9]))
    print("{:^15}{:^15}{:^15}".format(*values[9:12]))
    print("{:^15}{:^15}{:^15}".format(*values[12:15]))
    print("{:^15}{:^15}{:^15}".format(*values[15:18]))
    print("{:^15}{:^15}{:^15}".format(*values[18:21]))
    print("{:^15}{:^15}{:^15}".format(*values[21:24]))
    print("{:^15}{:^15}{:^15}".format(*values[24:27]))
    print("{:^15}{:^15}{:^15}".format(*values[27:30]))

#get the data
data = requests.get('https://www.basketball-reference.com/leagues/NBA_2019_leaders.html')

# load the data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

# pull data by element name




# Presents top 10 assist leaders of 2019 season
def astLeader():
    print('NBA Assists Per Game Leaders of 2019 Season:')
    for i in soup.find_all('div', {'id' : 'leaders_ast_per_g'}):
        # for x in i.find_all('td'):
        #     print(x)
        values = [x.text for x in i.find_all('td')] #using list comprehension. same as the block of text below:
        ast = values
        printBoard(ast)
        # for x in i.find_all('td'):
        #     values.append(x.text)

        # data.append(values)

def ptsLeader():
    print('NBA Points Per Game Leaders of 2019 Season:')
    for i in soup.find_all('div', {'id' : 'leaders_pts_per_g'}):
        values = [x.text for x in i.find_all('td')] #using list comprehension. same as the block of text below:
        pts = values
        printBoard(pts)

def rebLeader():
    print('NBA Rebounds Per Game Leaders of 2019 Season:')
    for i in soup.find_all('div', {'id' : 'leaders_trb_per_g'}):
        values = [x.text for x in i.find_all('td')] #using list comprehension. same as the block of text below:
        reb = values
        printBoard(reb)

def blkLeader():
    print('NBA Blocks Per Game Leaders of 2019 Season:')
    for i in soup.find_all('div', {'id' : 'leaders_blk_per_g'}):
        values = [x.text for x in i.find_all('td')]
        blk = values
        printBoard(blk)

def stlLeader():
    print('NBA Steals Per Game Leaders of 2019 Season:')
    for i in soup.find_all('div', {'id': 'leaders_stl_per_g'}):
        values = [x.text for x in i.find_all('td')]
        stl = values
        printBoard(stl)

def toLeader():
    print('NBA Turnover Leaders of 2019 Season:')
    for i in soup.find_all('div', {'id': 'leaders_tov'}):
        values = [x.text for x in i.find_all('td')]
        to = values
        printBoard(to)

def mpLeader():
    print('NBA Minutes Played Leaders of 2019 Season:')
    for i in soup.find_all('div', {'id': 'leaders_mp'}):
        values = [x.text for x in i.find_all('td')]
        mp = values
        printBoard(mp)

def fgp3Leader():
    print('NBA 3-pt Field Goal Pct Leaders of 2019 Season:')
    for i in soup.find_all('div', {'id': 'leaders_fg3_pct'}):
        values = [x.text for x in i.find_all('td')]
        fgp3 = values
        printBoard(fgp3)

def ftpLeader():
    print('NBA Free Throw Pct Leaders of 2019 Season:')
    for i in soup.find_all('div', {'id': 'leaders_ft_pct'}):
        values = [x.text for x in i.find_all('td')]
        ftp = values
        printBoard(ftp)

def fgpLeader():
    print('NBA Field Goal Pct Leaders of 2019 Season:')
    for i in soup.find_all('div', {'id': 'leaders_fg_pct'}):
        values = [x.text for x in i.find_all('td')]
        fgp = values
        printBoard(fgp)

def displayIntro():
    print('')
    print('-' * 90)
    print('{:^45}'.format('Welcome to the NBA Basketball Reference Top 10 Leaderboards of the 2019 NBA season!'))
    print('-' * 90)
    print('')
    print('Please select which stat leaderboard you would like to see:')
    print('1: Points \n2: Assists \n3: Rebounds \n4: Blocks \n5: Steals \n6: Turnovers \n7: Minutes Played \n8: 3-Pt FG Percentage \n9: Free Throw Percentage \n10: Field Goal Percentage')
    selection = input('->')
    print('')
    if selection == '1':
        ptsLeader()
    elif selection == '2':
        astLeader()
    elif selection == '3':
        rebLeader()
    elif selection == '4':
        blkLeader()
    elif selection == '5':
        stlLeader()
    elif selection == '6':
        toLeader()
    elif selection == '7':
        mpLeader()
    elif selection == '8':
        fgp3Leader()
    elif selection == '9':
        ftpLeader()
    elif selection == '10':
        fgpLeader()



playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y' or playAgain == 'Yes' or playAgain == 'Y':

    displayIntro()

    print()
    print('Would you like to see another leaderboard? (Yes or No)')
    playAgain = input()





# astLeader()
# ptsLeader()
# rebLeader()

# pprint(data)

# print(type(values))

nba_list = []





# print(nba_list)


# for i in values[0:3]:
#     first = i
#     nba_list.append(first)

# print(nba_list[1])
# print(values)

# print(type(data))
# print(data[0:1])
