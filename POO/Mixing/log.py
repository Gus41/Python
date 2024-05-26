#Abstração
from pathlib import Path
from abc import ABC, abstractmethod


LOG_FILE = Path(__file__).parent / 'log.txt'
# Pasta do projeto + O local do arquivo





class Log(ABC):
    
    @abstractmethod
    def _log(self,msg):
        ...

    def LogError(self,msg):
        self._log(f'Error : {msg}')

    def logSucces(self,msg):
        self._log(f'Succes: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        with open(LOG_FILE, 'a') as arq:
            arq.write(msg)
            arq.write("\n")
        print("msg foi salvo no log.txt")

 
if __name__ == '__main__':
    l = LogFileMixin()
    l.logSucces("Testing")
    print(LOG_FILE)