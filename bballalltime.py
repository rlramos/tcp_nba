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


# pulling data for most games
data_games = requests.get('https://www.basketball-reference.com/leaders/pts_career.html')
# creating a bs4 object of the most games data
soup_games = BeautifulSoup(data_games.text, 'html.parser')

def mostGames():
    games_list = []
    print('NBA Career Leaders and Records for Games:')
    for i in soup_games.find_all('div', {'id': 'all_nba'}): # pull the data from page
        values = [x.text for x in i.find_all('td')] # find data under correct html tags
        games = values
        for l in games: # iterate through each element
            games_list.append(l.strip()) # strip '/n' from each element
        printBoard(games_list) # print using printBoard function

# pulling data for most points
pts_games = requests.get('https://www.basketball-reference.com/leaders/pts_career.html')
# create a bs4 object of most pts data
soup_pts = BeautifulSoup(pts_games.text, 'html.parser') #pulling html text file

def mostPts(): # define function
    pts_list = [] # create a separate list for points
    print('NBA Career Leaders and Records for Points:')
    for i in soup_pts.find_all('div', {'id':'all_nba'}): #iterate through HTML code
        values = [x.text for x in i.find_all('td')] # and pull text from correct tag location to a separate list
        pts = values
        for k in pts: # iterate through each element in new list and remove '\n' from each element
            pts_list.append(k.strip())
        printBoard(pts_list) # use printBoard function to display modifed text from HTML code.

# pulling data for most assists accumulated
data_ast = requests.get('https://www.basketball-reference.com/leaders/ast_career.html')
# creating a bs4 object for assists data
soup_ast = BeautifulSoup(data_ast.text, 'html.parser')

def mostAst():
    ast_list = [] # create a list for modified ast data
    print('NBA Career Leaders and Records for Assists')
    for i in soup_ast.find_all('div', {'id':'all_nba'}): # iterate through html code under 'div' and 'id' tags
        ast = [x.text for x in i.find_all('td')] #use list comprehension to create a new list by pulling the x.text from for loop arguing 'td' tag in html code
        for k in ast: # loop through list and strip from each element ('/n')
            ast_list.append(k.strip())
        printBoard(ast_list)

data_reb = requests.get('https://www.basketball-reference.com/leaders/trb_career.html')
soup_reb = BeautifulSoup(data_reb.text, 'html.parser')

def mostReb():
    reb_list = [] # create a list for modified reb data
    print('NBA Career Leaders for Records for Total Rebounds')
    for i in soup_reb.find_all('div', {'id':'all_nba'}):
        reb = [x.text for x in i.find_all('td')]
        for k in reb:
            reb_list.append(k.strip())
        printBoard(reb_list)

data_blks = requests.get('https://www.basketball-reference.com/leaders/blk_career.html') # pull data from link
soup_blks = BeautifulSoup(data_blks.text, 'html.parser') # create a bs4 object

def mostBlks(): # def blks function
    blk_list = [] # create a list for the modified data
    print('NBA Career Leaders for Records for Total Rebounds')
    for i in soup_blks.find_all('div', {'id':'all_nba'}): # loop through bs4 object for 'div', {'id':'all_nba'}
        blks = [x.text for x in i.find_all('td')] # create 'blk' list by pulling x.text after for loop to find_all('td')
        for k in blks: # loop through list once more to remove excess space and '\n'
            blk_list.append(k.strip()) # adding to the list after striping string.
        printBoard(blk_list)

data_stl = requests.get('https://www.basketball-reference.com/leaders/stl_career.html')
soup_stl = BeautifulSoup(data_stl.text, 'html.parser')

def mostStls():
    stl_list = []
    print('NBA Career Leaders and Records for Steals')
    for i in soup_stl.find_all('div', {'id':'all_nba'}):
        stl = [x.text for x in i.find_all('td')]
        for k in stl:
            stl_list.append(k.strip())
        printBoard(stl_list)

data_ft = requests.get('https://www.basketball-reference.com/leaders/ft_career.html')
soup_ft = BeautifulSoup(data_ft.text, 'html.parser')

def mostFt():
    ft_list = []
    print('NBA Career Leaders and Records for Free Throws')
    for i in soup_ft.find_all('div', {'id':'all_nba'}):
        ft = [x.text for x in i.find_all('td')]
        for k in ft:
            ft_list.append(k.strip())
        printBoard(ft_list)

data_3pt = requests.get('https://www.basketball-reference.com/leaders/fg3_career.html') # pull data from link
soup_3pt = BeautifulSoup(data_3pt.text, 'html.parser') # create bs4 object

def most3pt(): # def most3pt function
    pt3_list = [] # create list
    print('NBA Career Leaders and Records for 3-Pt Field Goals')
    for i in soup_3pt.find_all('div', {'id':'all_nba'}): # loop through bs4 object finding argued tags. 'div', 'id':'all_nba'
        pt3 = [x.text for x in i.find_all('td')] # create a new list with text found from for loop using find_all function for 'td' tag
        for k in pt3: # loop through text pulled
            pt3_list.append(k.strip()) # adding elements from new text after stripping each element clean
        printBoard(pt3_list)

def displayIntro():
    print('')
    print('-' * 90)
    print('{:^45}'.format('Welcome to the Basketball Reference All Time Leaderboards'))
    print('-' * 90)
    print('')
    print('Please select which all time leaderboard you would like to see?')
    print('1. Points \n2. Assists \n3. Rebounds \n4. Blocks \n5. Steals \n6. Games Played \n7. Free Throws \n8. 3-pt Field Goals')
    selection = input('-->')
    print('')
    if selection == '1':
        mostPts()
    elif selection == '2':
        mostAst()
    elif selection == '3':
        mostReb()
    elif selection == '4':
        mostBlks()
    elif selection == '5':
        mostStls()
    elif selection == '6':
        mostGames()
    elif selection == '7':
        mostFt()
    elif selection == '8':
        most3pt()

playAgain = 'yes'
while playAgain == 'yes' or playAgain =='y' or playAgain == 'Yes' or playAgain == 'Y':

    displayIntro()

    print()
    print('Would you like to see another all-time leaderboard? (Yes or No)')
    playAgain = input()
    if playAgain == 'no' or playAgain =='No' or playAgain == 'n' or playAgain == 'N':
        print('Goodbye, nephew.')
