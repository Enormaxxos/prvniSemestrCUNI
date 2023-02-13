paletaTemplate = [] # kazdy box je delitelny 20, staci 6x6 mrizka, 20cm = 1unit
for i in range(6):
    paletaTemplate.append([])
    for j in range(6):
        paletaTemplate[i].append()

boxes = [int(i) for i in input().split()]

for boxType,boxCount in enumerate(boxes):
    boxSize = boxType + 1
    for i in range(boxCount):
        pass
        

with open('output.txt','w') as o:
    o.write(paletaTemplate)

class Paleta:
    def __init__(self):
        self.kolikFitnu = [False,36,9,4,1,1,1] # [isFull,20c still fits,40c,...,120c]

    def add6(self):
        self.kolikFitnu = [True] + 6*[None]
        return True

    def add5(self):
        self.kolikFitnu[1] -=25
        self.kolikFitnu[2] = 0
        self.kolikFitnu[3] = 0
        self.kolikFitnu[4] = 0
        self.kolikFitnu[5] = 0
        self.kolikFitnu[6] = 0

    def add4(self):
        self.kolikFitnu[1] -= 16
        self.kolikFitnu[2] -= 4
        self.kolikFitnu[3] = 0
        self.kolikFitnu[4] = 0
        self.kolikFitnu[5] = 0
        self.kolikFitnu[6] = 0

    def add3(self):
        self.kolikFitnu[1] -= 9
        self.kolikFitnu[2] -= 4
        self.kolikFitnu[3] -= 1
        self.kolikFitnu[4] = 0
        self.kolikFitnu[5] = 0
        self.kolikFitnu[6] = 0

    def add2(self):
        self.kolikFitnu[1] -= 4
        self.kolikFitnu[2] -= 1
        self.kolikFitnu[3] = 0
        self.kolikFitnu[4] = 0
        self.kolikFitnu[5] = 0
        self.kolikFitnu[6] = 0

    def add1(self):
        