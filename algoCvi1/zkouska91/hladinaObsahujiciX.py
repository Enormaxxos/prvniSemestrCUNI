from collections import deque

class VrcholBinStromu:
    """třída pro reprezentaci vrcholu binárního stromu"""
    def __init__(self, info = None, levy = None, pravy = None):
        self.info = info      # data
        self.levy = levy      # levé dítě 
        self.pravy = pravy    # pravé dítě

def hladina(koren : VrcholBinStromu, x : int) -> list[int] :
    """
    koren : kořen zadaného binárního stromu
    x     : zadané ohodnocení hledaného vrcholu
    vrátí : seznam čísel vrcholů na hladině obsahující x
    """

    # zalozim si dva nove seznamy, do jednoho (startovniho) vlozim koren
    lists = [[],[]]
    currentList = 0
    lists[currentList].append(koren)

    looping = True

    # while opakovani nize probiha dokud se nenajde x ve vrstve stromu nebo dokud existuje dalsi vrstva, kterou 
    # bych mohl prochazet
    while looping:
        looping = False
        layerHasX = False

        #projdu kazdy vrchol v momentalnim zasobniku, jejich deti vlozim do druheho zasobniku
        for vrchol in lists[currentList]:
            if vrchol.levy != None:
                looping = True
                if vrchol.levy.info == x:
                    layerHasX = True

                lists[(currentList + 1) % 2].append(vrchol.levy)

            if vrchol.pravy != None:
                looping = True
                if vrchol.pravy.info == x:
                    layerHasX = True

                lists[(currentList + 1) % 2].append(vrchol.pravy)

        # pokud nyni vystavena vrstva obsahuje hledane x, vrat seznam cisel ve vrstve, pokud ne, momentalni vymaz a prohod zasobniky
        if layerHasX:
            return [unit.info for unit in lists[(currentList + 1) % 2]]
        else:
            lists[currentList].clear()
            currentList = (currentList + 1) % 2

    # pokud se x nenajde za dobu celeho prubehu, vrat prazdny seznam
    return list()