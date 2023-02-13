n = int(12)

for i in range(n):
    for j in range(n):
        print((i+j) % n,end=" ")
    print()

input("...")

for i in range(n):
    for j in range(n):
        print((i*j) % n,end=" ")
    print()
