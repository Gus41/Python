#Abstração
class Log:
    def log(self,msg):
        raise NotImplemented("Implemente o metodo Log")

class LogFileMixin(Log):
    ...

 
if __name__ == 'main':
    l = Log()
    l.log()