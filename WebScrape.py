#This program will take user's input for players, search for their stats
# on NBAreference.com, then create excel files for those stats


import urllib
from bs4 import BeautifulSoup
import os
import xlwt

url_list = []
players = []
row = []

def wsSetup():
"""This function is incomplete but goal is to set up ws with correct column 
	and row titles """
	wb = xlwt.Workbook()
	ws = wb.add_sheet('Stat Sheet')
		
def make_soup(url):
	"""Opens page and creates BeautifulSoup object"""
	page = urllib.urlopen(url)
	soupdata = BeautifulSoup(page, "html.parser")
	return soupdata
	
def retrieveStats(url_list, players):
	"""In the BeautifulSoup object, draw out all stats and insert into excel file"""
	player = 0 
	for url in url_list:
		wb = xlwt.Workbook()
		ws = wb.add_sheet('Stat Sheet')
		soup = make_soup(url)
		x, y = 0, 1 
	
		for table in soup.find_all(id = 'pgl_basic'):
			for record in table.find_all('tr'):
				for stat in record.find_all('td'):
					if stat.text == 'Did Not Play' or stat.text == 'Inactive':
						ws.write(x, y, stat.text)
						x = 0
						y += 1
					elif x < 30:
						ws.write(x, y, stat.text)
						x += 1
					else:
						ws.write(x, y, stat.text)
						x = 0
						y += 1
		wb.save('{}.xls'.format(players[player]))
		player += 1		

def getUrls(players):
	"""Creates custom URL for each player"""
	for player in players:
		nameLi = player.split(" ")
		firstName = nameLi[0]
		lastName = nameLi[1]
		firstletter = lastName[0].lower()
		first2letter = (firstName[0] + firstName[1]).lower()
		final = (lastName[:5] + first2letter).lower()
		url = "http://www.basketball-reference.com/players/{}/{}01/gamelog/2016/".format(firstletter, final)
		url_list.append(url)

while True:
"""Asks user to input players"""
	player = raw_input("Enter players.  Enter 'Done' when finished   ")
	if player.lower() == 'done':
		break
	else:
		players.append(player)
		os.system('clear')
		print "Current Players: {}".format(players)
		
		
getUrls(players)
print url_list
try:
	retrieveStats(url_list, players)

except:
	print "This network request did not work dude"
				
