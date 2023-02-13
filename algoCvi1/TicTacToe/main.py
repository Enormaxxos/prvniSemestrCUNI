import tkinter

boardN = 3

board = []

for i in range(boardN):
    board.append([])
    for j in range(boardN):
        board[i].apppend(None)

canvW = 400
canvH = 400
lineW = 2
blankSpaceX = canvW // 50
blankSpaceY = canvH // 50

main = tkinter.Canvas(width=canvW, height=canvH, bg="black")
main.pack()

main.create_line(canvW // 3, 0, canvW // 3, canvH, fill="white", width=lineW)
main.create_line(canvW // 3 * 2, 0, canvW // 3 * 2, canvH, fill="white", width=lineW)
main.create_line(0, canvH // 3, canvW, canvH // 3, fill="white", width=lineW)
main.create_line(0, canvH // 3 * 2, canvW, canvH // 3 * 2, fill="white", width=lineW)

currPlayer = 0

def drawX(pos):
    oneStart = (pos[0] * (canvW // 3) + blankSpaceX,pos[1] * (canvW // 3) + blankSpaceY)
    oneEnd = ((pos[0] + 1) * (canvW // 3) - blankSpaceX,(pos[1] + 1) * (canvW // 3) - blankSpaceY)
    twoStart = ((pos[0] + 1) * (canvW // 3) - blankSpaceX,(pos[1]) * (canvW // 3) + blankSpaceY)
    twoEnd = ((pos[0]) * (canvW // 3) + blankSpaceX,(pos[1] + 1) * (canvW // 3) - blankSpaceY)

    main.create_line(oneStart[0],oneStart[1],oneEnd[0],oneEnd[1],fill= "white",width=lineW)
    main.create_line(twoStart[0],twoStart[1],twoEnd[0],twoEnd[1],fill= "white",width=lineW)

def drawO(pos):
    oneStart = (pos[0] * (canvW // 3) + blankSpaceX,pos[1] * (canvW // 3) + blankSpaceY)
    oneEnd = ((pos[0] + 1) * (canvW // 3) - blankSpaceX,(pos[1] + 1) * (canvW // 3) - blankSpaceY)

    main.create_oval(oneStart[0],oneStart[1],oneEnd[0],oneEnd[1],outline="white",fill="black",width=lineW)

def drawWinLine():


def checkBoard():
    def checkDiag():
        isSame = all([board[0][0] == board[i][i] for i in range(boardN)])
        start
        return (isSame, board[0][0] if isSame else None)

    def checkOtherDiag():
        isSame = all([board[boardN-1][0] == board[boardN-i-1][i] for i in range(boardN)])
        return (isSame, board[boardN-1][0] if isSame else None)

    def checkLine(lineNum):
        isSame = all(board[lineNum][0] == board[lineNum][i] for i in range(boardN))
        return (isSame,board[lineNum][0] if isSame else None)

    def checkColumn(columnNum):
        isSame = all(board[0][columnNum] == board[i][columnNum] for i in range(boardN))
        return (isSame,board[0][columnNum] if isSame else None)


def clickedEvent(pos):
    global currPlayer
    clickIndeces = (pos.x //( canvW // 3 ), pos.y // (canvH // 3 ))

    if currPlayer == 0:
        board[clickIndeces[0]][clickIndeces[1]] = "X"
        drawX(clickIndeces)
    else:
        board[clickIndeces[0]][clickIndeces[1]] = "O"
        drawO(clickIndeces)

    checkBoard()

    currPlayer = (currPlayer + 1) % 2

    print(board)


main.bind("<Button-1>", clickedEvent)
main.mainloop()
