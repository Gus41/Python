import requests
from bs4 import BeautifulSoup
from datetime import date
import customtkinter


def init():

    def appendEvents(events:list):
        for e in events:
            if e[0] != None and e[1] != None:
                d = customtkinter.CTkLabel(frame,text=e[0])
                t = customtkinter.CTkLabel(frame,text=e[1])
                separator = customtkinter.CTkLabel(frame,text='------')

                t.pack(padx=40,pady=10)
                d.pack(padx=40,pady=10)
                separator.pack(padx=40,pady=30)
        

    
    url = 'https://www.ucs.br/site/eventos/'
    header = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0'}
    page = requests.get(url,headers= header)
    soup = BeautifulSoup(page.content,'html.parser')

    def searchEvents():
        box = soup.find('div',{'class': 'box_cinza_claro'})
        links = box.find_all('a') # type: ignore
        events = []
        for e in links:
            link = e['href']
            if 'site/eventos' in link:
                eventLink = 'https://www.ucs.br/' + link
                pageEvent = requests.get(url=eventLink,headers=header)
                eventContent = BeautifulSoup(pageEvent.content,'html.parser')
                eventDate = eventContent.find('h3')
                eventTittle = eventContent.find('h4')
                eventDate = eventDate.text # type: ignore
                if eventTittle != None:
                    eventTittle = eventTittle.text
                    
                event = [eventTittle, eventDate]
                events.append(event)
        
        return events
    
    
    allEvents = searchEvents()
    atualDay = date.today().day
    atualMonth = date.today().month
    appendEvents(allEvents)


window = customtkinter.CTk()
window.geometry("900x500")

tittle = customtkinter.CTkLabel(window,text="Eventos")
tittle.pack(padx=10,pady=10)
button = customtkinter.CTkButton(window,text="Procurar eventos", command=init)
button.pack(padx=10,pady=10)
frame = customtkinter.CTkScrollableFrame(window,width=800,height=350)

frame.pack()

window.mainloop()


