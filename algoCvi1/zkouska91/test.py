a = [0,1,-2,-1,3,2,-3]
aSorted = a.sort(key=lambda x: abs(x))

minimal = 0
kladne = False
zaporne = False


for i in range(len(a)):
    prvek = a[i]
    if prvek == 0 and minimal == 0:
        minimal = 1
    if abs(prvek) == minimal and prvek < 0:
        zaporne = True
        if kladne == True:
            kladne, zaporne = False,False
            minimal += 1
    if abs(prvek) == minimal and prvek > 0:
        kladne = True
        if zaporne == True:
            kladne, zaporne = False,False
            minimal += 1
    if abs(prvek) > minimal:
        if kladne == False:
            print( minimal )
            break
        if zaporne == False:
            print( -minimal )
            break