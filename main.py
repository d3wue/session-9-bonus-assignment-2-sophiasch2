import requests
import bs4

userAgent = {
'User-Agent' :
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

#while True:
#print ("menu:")
#print("1. Show available teams")
#print("2.Select team and show high level information on the team")
#print(" 3. Select team and and show all players of the team")
#print(" 4. Stop the program")
# userInput=
#int (input("enter number: › "))
#if userInput==1:

url ="https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1"
r = requests.get(url, headers=userAgent)
if r.status_code == 200:
    htmlText = r.text
    htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser')

    table =htmlDocument.find('table', {'class': 'items'}).find('tbody')
    teams=table.find_all('tr')

    for team in teams:
#team=teams [0] (nur das erste)
        teamName=team.find('td',{'class': 'hauptlink no-border-links'}).get_text()
        squad=team.find('td', )
        print (teamName)
