import math

def sito(n):
    prvocisla = []
    je_prv = [False,False,True,True] + int(((n-0.5)//2)-1)*[True]
    for p in range(2,int((n-0.5)//2)+3):
        if je_prv[p]:
            prvocisla.append(p if p<=3 else p+(p-3))
            if p == 2:
                continue
            for i in range(p,int((n-0.5)//2)+3,1+(p-2)*2):
                je_prv[i] = False
    return prvocisla

a = int(input())
orig = a

primes = sito(a)

factors = []

while a not in primes:
    print(f"a: {a}")
    for i in range(len(primes)):
        if a % primes[i] == 0:
            a = a // primes[i]
            factors.append(primes[i])
            break

factors += [a]

final = f"{orig}="
for i in range(len(factors)):
    final += f"{factors[i]}{'*' if i < len(factors)-1 else ''}"

print(final)