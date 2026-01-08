from collections import defaultdict

lines = []

with open("C:/Users/Franco/Documents/adventofcode2025/dia9/inputdia9.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.rstrip("\n"))

def calculateArea(square1,square2):

    height = max(square1[1],square2[1]) + 1 - min(square1[1],square2[1])
    base = max(square1[0],square2[0]) + 1 - min(square1[0],square2[0])

    return base * height

def isValidRectangle(square1,square2):

    if square1[0] == square2[0] or square1[1] == square2[1]:
        return False

    xinit  = min(square1[0],square2[0])
    xend = max(square1[0],square2[0])
    yinit  = min(square1[1],square2[1])
    yend = max(square1[1],square2[1])

    for n in range(yinit,yend+1):
        if n in horizontalRanges:
            for h in range(len(horizontalRanges[n])):
                if horizontalRanges[n][h][0] <= xinit and xend <= horizontalRanges[n][h][1]:
                    break
                if h == (len(horizontalRanges[n]) - 1):
                    return False
        else:
            return False
        
    return True

def extendHorizontalrange(n,minimo,maximo):
    for h in range(len(horizontalRanges[n])):
        horizontalRange = horizontalRanges[n][h]
        if minimo <= horizontalRange[1] and horizontalRange[1] <= maximo:
            horizontalRanges[n][h] = [min(minimo,horizontalRange[0]),max(maximo,horizontalRange[1])]
        elif horizontalRange[0] <= maximo and maximo <= horizontalRange[1]:
            horizontalRanges[n][h] = [min(minimo,horizontalRange[0]),max(maximo,horizontalRange[1])]
        elif horizontalRange[1] < minimo or maximo < horizontalRange[0]:
            horizontalRanges[n].append([minimo,maximo])


print("#CREAMOS LA LISTA DE CUADRADOS   ") 
redSquares = []
for line in lines:
    parts = line.split(",")
    parts[0] = int(parts[0])
    parts[1] = int(parts[1])
    redSquares.append(parts)

print("CREAMOS LOS RANGOS VERTICALES")
verticalRanges = {}

for n in range(len(redSquares)):
    
    currentSquare = redSquares[n]
    nextSquare = None
    if n == len(redSquares) - 1:
        nextSquare = redSquares[0]
    else:
        nextSquare = redSquares[n+1]

    if currentSquare[0] == nextSquare[0]:
        minimo = min(currentSquare[1],nextSquare[1])
        maximo = max(currentSquare[1],nextSquare[1])
        if currentSquare[0] in verticalRanges:
            verticalRanges[currentSquare[0]].append([minimo,maximo])
        else:
            verticalRanges[currentSquare[0]] = [[minimo,maximo]]

print("CREAMOS LOS RANGOS HORIZONTALES")
horizontalRanges = {}

for key in verticalRanges:
    verticalRange = verticalRanges[key][0]
    for n in range(verticalRange[0],verticalRange[1]+1):
        for key2 in verticalRanges:
            if key != key2:
                otherVerticalRange =  verticalRanges[key2][0]
                if otherVerticalRange[0] <= n and n <= otherVerticalRange[1]:
                    minimo = min(key,key2)
                    maximo = max(key,key2)
                    if n in horizontalRanges:
                        extendHorizontalrange(n,minimo,maximo)
                    else:
                        horizontalRanges[n] = [[minimo,maximo]]

print("CREAMOS LAS AREAS Y LASORDENAMOS" )

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

print("buscamos la mas grande valida")

for n in range(len(listaDeAreaPuntos)):
    rectangulos = listaDeAreaPuntos[len(listaDeAreaPuntos) - 1 - n]
    print("ahora va" + str(n) + " de " +str(len(listaDeAreaPuntos)))
    
    if isValidRectangle(rectangulos[1][0],rectangulos[1][1]):
        maxArea = rectangulos[0]
        break

print(maxArea)
