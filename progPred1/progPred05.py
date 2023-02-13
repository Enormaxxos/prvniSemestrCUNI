from math import sqrt

class Prvek:
    def __init__(self,x,dalsi):
        self.x = x
        self.dalsi = dalsi


class LLS:
    def __init__(self):
        self.zac = None

    def show(self):
        p = self.zac
        while p != None:
            print(p.x)
            p = p.dalsi
        print("--end--")

    def addStart(self,val):
        self.zac = Prvek(val,self.zac)

    def removeStart(self):
        if self.zac == None:
            return
        self.zac = self.zac.dalsi

    def addEnd(self,val):
        p = self.zac

        if p == None:
            self.addStart(val)
            return

        while p.dalsi != None:
            p = p.dalsi
        
        p.dalsi = Prvek(val,None)


    def removeEnd(self):
        predP = None
        p = self.zac

        if p == None:
            return
        elif p.dalsi == None:
            self.removeStart()
        

        while p.dalsi != None:
            predP = p
            p = p.dalsi

        predP.dalsi = None
        
        



seznam = LLS()
seznam.addStart(20)
seznam.addStart(30)
seznam.addStart(40)
seznam.show()
print("---")
seznam.removeStart()
seznam.removeStart()
seznam.removeStart()
seznam.show()
print("---")




























class Komplex:
    def __init__(self,re=0,im=0):
        self.re = re
        self.im = im

    def abs(self):
        return sqrt(self.re ** 2 + self.im ** 2)

    def toString(self):
        return f""

    
k = Komplex(re=4)