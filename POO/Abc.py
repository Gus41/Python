from abc import ABC,abstractmethod



class Notification(ABC):
    def __init__(self,mensagem) -> None :
        self._mensagem = mensagem
    
    @abstractmethod
    def send(self) -> bool:...

class Sms(Notification):
    def send(self) -> True:  # type: ignore
        print(self._mensagem)
        return True

def notificar(mensagem:Notification):
    enviada = mensagem.send()

    if enviada :
        print("Notificação enviada")
    else : 
        print("Falha em enviar mensagem")

notificar(Sms("Testando"))