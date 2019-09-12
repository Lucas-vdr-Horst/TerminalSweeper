import random

aroundX = [0, 1, 1, 1, 0, -1, -1, -1]
aroundY = [1, 1, 0, -1, -1, -1, 0, 1]

def withinBoundaries(checkField, x, y):
    return y < len(checkField[0]) and y >= 0 and x < len(checkField) and x >= 0

def checkRelative(checkField, x, y, relativeX, relativeY):
    if withinBoundaries(checkField, x + relativeX, y + relativeY):
        if checkField[x + relativeX][y + relativeY] == 'x':
            return True
        else:
            return False
    else:
        return False

def minesSerounding(checkField, x, y):
    serounding = 0
    for s in range(8):
        if (checkRelative(checkField, x, y, aroundX[s], aroundY[s])):
            serounding += 1
    checkField[x][y] = str(serounding)
    if (serounding == 0):
        for a in range(8):
            newX = x + aroundX[a]
            newY = y + aroundY[a]
            if withinBoundaries(checkField, newX, newY):
                if(checkField[newX][newY] == ' '):
                    checkField = minesSerounding(checkField, newX, newY)
    return checkField

def countEmpty(checkField):
    countedEmpty = 0
    for c in range(len(checkField)):
        countedEmpty += checkField[c].count(' ')
    return countedEmpty

def printField(prtField):
    print()
    numberLineWidth = range(width)
    numberLineHeight = range(height)
    line = "   "
    for w in range(width):
        line += ' ' + str(numberLineWidth[w])
        if len(str(numberLineWidth[w])) < 2:
            line += ' '
    print(line)
    for y in range(len(prtField[0])):
        line = ""
        for x in range(len(prtField)):
            char = prtField[x][y]
            if char == 'x':
                char = ' '
            line += '[' + char + ']'
        strNumberLine = ' ' + str(numberLineHeight[y])
        if len(str(numberLineHeight[y])) < 2:
            strNumberLine += ' '
        print(strNumberLine + line)

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def getInfo(question):
    return input(question)

def getInfoNumber(question, min, max):
    while True:
        rawInfo = getInfo(question)
        if (not is_number(rawInfo)):
            print("Awnser is not a (whole) number")
        elif (int(rawInfo) < min):
            print("Number to small, min: " + str(min))
        elif (int(rawInfo) > max):
            print("Number to large, max: " + str(max))
        else:
            return int(rawInfo)

width = getInfoNumber("Field width: ", 2, 50)
height = getInfoNumber("Field height: ", 2, 50)
numberMines = getInfoNumber("Number of mines: ", 1, width * height)

#Create field
field = []
for v in range(width):
    line = []
    for h in range(height):
        line.append(' ')
    field.append(line)
for m in range(numberMines): #Create mines
    placed = False
    while not placed:
        rndX = random.randint(0, width -1)
        rndY = random.randint(0, height -1)
        if field[rndX][rndY] == ' ':
            field[rndX][rndY] = 'x'
            placed = True

gameOver = False
while not gameOver:
    printField(field)

    checkX = getInfoNumber("Check X: ", 0, width - 1)
    checkY = getInfoNumber("Check Y: ", 0, height -1)
    if field[checkY][checkY] == 'x':
        print("Game Over")
        gameOver = True
    else:
        field = minesSerounding(field, checkX, checkY)
    if(countEmpty(field) == 0 and not gameOver):
        printField(field)
        print("You win!")
        gameOver = True
