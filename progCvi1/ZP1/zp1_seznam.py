class Seznam:
    def __init__(self):
        self.seznam = []

    def pridej(self,value):
        self.seznam.append(value)

    def odeber(self,value):
        try:
            self.seznam.remove(value)
        except:
            return

    def setrid(self):
        self.seznam.sort(reverse=True)

    def vypis(self):
        for value in self.seznam:
            print(value)

seznam = Seznam()

while True:
    inS = input()

    instrukce,*args = inS.split()

    if instrukce == '1':
        seznam.pridej(int(args[0]))

    if instrukce == '2':
        seznam.odeber(int(args[0]))

    if instrukce == '4':
        seznam.setrid()

    if instrukce == '5':
        seznam.vypis()

    if instrukce == '6':
        break
    
