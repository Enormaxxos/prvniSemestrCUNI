from math import ceil

def justify(text, width):
    final = ""
    textParts = text.split(" ")
    
    lines = [[[],0]]
    
    for i in range(len(textParts)):
        if lines[-1][1] + len(textParts[i]) <= width - max(0,len(lines[-1][0])):
            lines[-1][0].append(textParts[i])
            lines[-1][1] += len(textParts[i])
        else:
            lines.append([[],0])
            lines[-1][0].append(textParts[i])
            lines[-1][1] += len(textParts[i])


    for i in range(len(lines)):
        lineStr = ""
        spaceC = len(lines[i][0])-1
        spacesToBePlaced = width-lines[i][1]
        spaces = []

        while spaceC != 0:
            spaces.append(ceil(spacesToBePlaced/spaceC))
            spaceC -= 1
            spacesToBePlaced -= spaces[-1]

        
        for j in range(len(spaces)):
            lineStr += lines[i][0][j]
            lineStr += " " * (spaces[j] if i != len(lines)-1 else 1)

        lineStr += lines[i][0][-1]
        lineStr += ("\n" if i != len(lines)-1 else "")
        final += lineStr
    return final


print(justify("""Codewars is a platform that helps you learn, train, and improve your coding skills by solving programming tasks of many types and difficulty levels. You choose how you would like to learn. Do you want to take on increasingly difficult challenges? Maybe you prefer training through repetition and by improving your solutions. After solving a task, compare your answer with other users and learn from them or help less experienced users by answering their questions.""",30))