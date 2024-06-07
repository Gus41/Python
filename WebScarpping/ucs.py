import requests
from bs4 import BeautifulSoup
from datetime import date

def init():

    def showEvents(events:list):
        for e in events:
            print("----")
            print(e)

    
    url = 'https://www.ucs.br/site/eventos/'
    header = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0'}
    page = requests.get(url,headers= header)
    soup = BeautifulSoup(page.content,'html.parser')

    def searchEvents():
        box = soup.find('div',{'class': 'box_cinza_claro'})
        links = box.find_all('a')
        events = []
        for e in links:
            link = e['href']
            if 'site/eventos' in link:
                eventLink = 'https://www.ucs.br/' + link
                pageEvent = requests.get(url=eventLink,headers=header)
                eventContent = BeautifulSoup(pageEvent.content,'html.parser')
                eventHeader = eventContent.find("header",{'class': 'bg-ft'})
                eventDate = eventContent.find('h3')
                eventTittle = eventContent.find('h4')
                eventDate = eventDate.text
                if eventTittle != None:
                    eventTittle = eventTittle.text
                    
                event = {eventTittle, eventDate}
                events.append(event)
        
        return events
    
    
    allEvents = searchEvents()
    showEvents(allEvents)
    atualDay = date.today().day
    atualMonth = date.today().month
    print(f'{atualDay} de {atualMonth}')
init()
