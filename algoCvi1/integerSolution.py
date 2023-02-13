import math

def integerSolution(a,b):

    solutions = []
    #X+Y = a
    #Y = a-X
    #X*(a-X) = b

    #X**2-aX+b=0

    #d=a**2 - 4 * 1 * b
    #d=a**2 -4*b

    #x1 = -b-sqrt(d)/2a
    #x2 = -b+sqrt(d)/2a

    #x1 = -b-sqrt(a**2 -4*b)/2a
    #x2 = -b+sqrt(a**2 -4*b)/2a

    d = (-a)**2 - 4 * 1 * b
    try:
        sqrtD = math.sqrt(d)
    except ValueError:
        print("No solution")
        return
    #print(math.sqrt(d))

    x1 = (a - sqrtD)/2
    x2 = (a + sqrtD)/2

    tolerance = 0.001

    if abs(x1-round(x1)) < tolerance and abs(x2-round(x2)) < tolerance:
        #print([math.floor(x1),math.floor(x2)])
        print(f"X = {round(x1)}, Y = {round(x2)}")
        if round(x1) - round(x2) != 0:
            print(f"X = {round(x2)}, Y = {round(x1)}")

    else:
        print("No solution")


integerSolution(int(input()),int(input()))