#Abstração
class Log:
    def _log(self,msg):
        raise NotImplemented("Implemente o metodo Log")
    
    def LogError(self,msg):
        self._log(f'Error : {msg}')

    def logSucces(self,msg):
        self._log(f'Succes: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)

 
if __name__ == '__main__':
    l = LogFileMixin()
    l.LogError("Testing")