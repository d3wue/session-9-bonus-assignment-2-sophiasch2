import requests
import bs4

userAgent = {
'User-Agent' :
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

while True:
    print ("menu:")
    print("1. Show available teams")
    print("2. Select team and show information on the team")
    print("3. Stop the program")
    userInput=int(input("enter a number: > "))

    if userInput==1:
        url ="https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1"
        r = requests.get(url, headers=userAgent)
        if r.status_code == 200:
            htmlText = r.text
            htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser')
            table =htmlDocument.find('table', {'class': 'items'}).find('tbody')
            teams=table.find_all('tr')

            for team in teams:
                teamName=team.find('td',{'class': 'hauptlink no-border-links'}).get_text().strip()

                print(f"{teamName}")

    if userInput ==2:
        choice = int(input("index of the team. \n >>>"))
        url ="https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1"
        r = requests.get(url, headers=userAgent)
        if r.status_code == 200:
            htmlText = r.text
            htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser')
            table =htmlDocument.find('table', {'class': 'items'}).find('tbody')
            teams=table.find_all('tr')
            
        team=teams[choice]
        teamName=team.find('td',{'class': 'hauptlink no-border-links'}).get_text().strip()
        info = team.find_all('td', {'class': 'zentriert'})
        squad = info[1].text
        age = info[2].text
        foreigners = info[3].text
        imfo = team.find_all('td', {'class': 'rechts'})
        averageMarketValue = imfo[0].text
        totalMarketValue = imfo[1].text
        print(f"{teamName}: squad: {squad}, age: {age}, foreigners: {foreigners}, averageMarketValue: {averageMarketValue}, totalMarketValue: {totalMarketValue}")
    
    if userInput == 3:
        break
  

