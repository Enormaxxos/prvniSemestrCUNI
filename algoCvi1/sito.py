def sito(n):
    returningList = (n) * [False]

    prvocisla = []
    je_prv = [False,False,True,True] + int(((n-0.5)//2)-1)*[True]
    for p in range(2,int((n-0.5)//2)+3):
        if je_prv[p]:
            prvocisla.append(p if p<=3 else p+(p-3))
            returningList[p if p<=3 else p+(p-3)] = True
            if p == 2:
                continue
            for i in range(p,int((n-0.5)//2)+3,1+(p-2)*2):
                je_prv[i] = False
    return prvocisla, returningList

n = 1000000

index=0

a,b = sito(n)

for i in range(n):
    if b[i] and not i in a:
        index += 1
        print(i, "is wrongly correct")
    if not b[i] and i in a:
        index += 1
        print(i, "is wrongly incorrect")
        


