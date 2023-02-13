maxN = int(input())

final = ""

def incrSeqs(n):

    def incrSqr(currN,currSeq):
        global final
        
        if len(currSeq) != 0:
            final += " ".join([str(val) for val in currSeq]) + "\n"
        for i in range(currN+1,maxN+1):
            incrSqr(i,currSeq.copy() + [i])

    incrSqr(0,[])

incrSeqs(maxN)

print(final[:-1])
