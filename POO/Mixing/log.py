#Abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'
# Pasta do projeto + O local do arquivo


class Log:
    def _log(self,msg):
        raise NotImplemented("Implemente o metodo Log")
    
    def LogError(self,msg):
        self._log(f'Error : {msg}')

    def logSucces(self,msg):
        self._log(f'Succes: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        with open(LOG_FILE, 'w') as arq:
            arq.write(msg)
            arq.write("\n")

 
if __name__ == '__main__':
    l = LogFileMixin()
    l.logSucces("Testing")
    print(LOG_FILE)