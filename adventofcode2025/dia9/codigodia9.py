from collections import defaultdict

lines = []

with open("C:/Users/Franco/Documents/adventofcode2025/dia9/inputdia9.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.rstrip("\n"))


def calculateArea(square1,square2):

    height = max(square1[1],square2[1]) + 1 - min(square1[1],square2[1])
    base = max(square1[0],square2[0]) + 1 - min(square1[0],square2[0])

    return base * height

def hasCloserUpward(topOne, y):
    x = topOne[0]

    for n in range(0,y+1):
        if n in orderedDictionaryRedSquares and (isRed(x,n) or isBetweenReds(x,n)):
            for h in range(n+1,topOne[1]):
                if not(h in orderedDictionaryRedSquares and (isRed(x,h) or isBetweenReds(x,h))):
                    break
            return True
    
    return False

def hasCloserDownward(bottomOne, y):

    x = bottomOne[0]

    for n in range(y,lastCol+1):
        if n in orderedDictionaryRedSquares and (isRed(x,n) or isBetweenReds(x,n)):
            for h in range(bottomOne[1]+1,n):
                if not(h in orderedDictionaryRedSquares and (isRed(x,h) or isBetweenReds(x,h))):
                    break
            return True
    
    return False
        
def isRed(x,y):
    if x in orderedDictionaryRedSquares[y]:
        return True
    return False
        
def isBetweenReds(x,y):
    
    redsToTheLeftCounter = 0
    redsToTheRightCounter = 0

    for elem in orderedDictionaryRedSquares[y]:
        if elem < x:
            redsToTheLeftCounter+=1
            

    if redsToTheLeftCounter % 2 == 0:
        return False
    
    for elem in orderedDictionaryRedSquares[y]:
        if x < elem:
            redsToTheRightCounter+=1

    return not redsToTheRightCounter % 2 == 0


def isValidRectangle(square1,square2):

    if square1[0] == square2[0] or square1[1] == square2[1]:
        return False

    topOne = None
    bottomOne = None
    if square1[1] <= square2[1]:
        bottomOne = square1
        topOne = square2
    else:
        bottomOne = square2
        topOne = square1

    if hasCloserUpward(topOne, bottomOne[1]) and hasCloserDownward(bottomOne,topOne[1]):
        return True
    
    return False

    
redSquares = []
for line in lines:
    parts = line.split(",")
    parts[0] = int(parts[0])
    parts[1] = int(parts[1])
    redSquares.append(parts)

lastRow = max(x[0] for x in redSquares)
lastCol = max(x[1] for x in redSquares)

areas = [[None for _ in range(len(redSquares))] for _ in range(len(redSquares))]
listaDeAreaPuntos = []

for n in range(len(redSquares)):
    print(str(n) + " de " + str(len(redSquares)))
    for h in range(len(redSquares)):
        if not n == h and areas[h][n] == None:
            area = calculateArea(redSquares[n],redSquares[h])
            areas[n][h] = area
            listaDeAreaPuntos.append([area, (redSquares[n], redSquares[h])])

listaDeAreaPuntos.sort(key=lambda x: x[0])

maxArea = None

orderedDictionaryRedSquares = defaultdict(list)

for a, b in redSquares:
    orderedDictionaryRedSquares[b].append(a)

for key in orderedDictionaryRedSquares:
    orderedDictionaryRedSquares[key].sort()

for n in range(len(listaDeAreaPuntos)):
    rectangulos = listaDeAreaPuntos[len(listaDeAreaPuntos) - 1 - n]
    print("ahora va" + str(rectangulos[1][0]) + str(rectangulos[1][1]))
    
    if isValidRectangle(rectangulos[1][0],rectangulos[1][1]):
        maxArea = rectangulos[0]
        break


print(maxArea)
