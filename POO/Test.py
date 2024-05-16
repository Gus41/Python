class Pessoa:
    def __init__(self,name):
        self.name = name

    def saiHy(self):
        print(f'{self.name} is saing hy!')

p1 = Pessoa("Teste")
p1.saiHy()

class Cam:
    def __init__(self,name,recording=False) -> None:
        self.name = name
        self.recording = recording
    
    def record(self)-> None:
        if self.recording:
            print("Arlredy recording")
            return
        self.recording = True
        print(f'{self.name} is recording')

    def photograph(self):
        if self.recording :
            print("Cant take a photo while recording")
            return
    def stopRecording(self):
        self.recording = False


canon = Cam("Canon")
canon.record()
print(canon.__dict__)
print(vars(canon))