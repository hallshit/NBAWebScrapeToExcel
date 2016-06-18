import urllib
from bs4 import BeautifulSoup
import os
import xlwt

url_list = []
players = []
row = []
wb = xlwt.Workbook()
ws = wb.add_sheet('Stat Sheet')



def make_soup(url):
	page = urllib.urlopen(url)
	soupdata = BeautifulSoup(page, "html.parser")
	return soupdata
	
def retrieveStats(url_list):
	for url in url_list:
		soup = make_soup(url)
		x, y = 0, 0 
		for table in soup.find_all(id = 'pgl_basic'):
			for record in table.find_all('tr'):
				for stat in record.find_all('td'):
					if x < 30:
						ws.write(x, y, stat.text)
						x += 1
					else:
						ws.write(x, y, stat.text)
						x = 0
						y += 1
		wb.save('{}'.format('stats2.xls'))
				

def getUrls(players):
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
	player = raw_input("Enter players.  Enter 'Done' when finished   ")
	if player.lower() == 'done':
		break
	else:
		players.append(player)
		os.system('clear')
		print "Current Players: {}".format(players)
		
		
getUrls(players)
print url_list
retrieveStats(url_list)

			
