import sys

lines = []

with open("C:/Users/Franco/Documents/adventofcode2025/dia8/inputdia8.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.rstrip("\n"))

def wasTheconnectionAlreadyMade(firstJunction,secondJunction,distances):
    for key in distances:
        if firstJunction in key[0] and secondJunction in key[0]:
            return True
    
    return False

def wasTheconnectionAlreadyMadev2(firstJunction,secondJunction,distances):
    for key in distances:
        if firstJunction in key and secondJunction in key:
            return True
    
    return False

def euclidianDistance(firstJunction,secondJunction):

    firstValSquared = (int(firstJunction[0]) - int(secondJunction[0])) ** 2
    secondtValSquared = (int(firstJunction[1]) - int(secondJunction[1])) ** 2
    thirdValSquared = (int(firstJunction[2]) - int(secondJunction[2])) ** 2

    sumaDeLosTres = firstValSquared + secondtValSquared + thirdValSquared

    return sumaDeLosTres

junctionBoxes = []
for line in lines:
    parts = line.split(",")
    junctionBoxes.append(parts)

matrixOfJunctionBoxes = [[None for _ in range(len(junctionBoxes))] for _ in range(len(junctionBoxes))]


for n in range(len(junctionBoxes)):
    print(n)
    for h in range(len(junctionBoxes)):
        if h!=n and matrixOfJunctionBoxes[h][n] == None:
            distance =  euclidianDistance(junctionBoxes[h],junctionBoxes[n])
            matrixOfJunctionBoxes[n][h] = distance



cantidadDeConexiones  = 1000

connectionsMade = []

connectedJunctionBoxes = []

for i in range(cantidadDeConexiones):
    currentSmallestConnection = sys.maxsize
    connectedBoxes = None,None
    for n in range(len(matrixOfJunctionBoxes)):
        for h in range(n+1,len(matrixOfJunctionBoxes[n])):
            distance = matrixOfJunctionBoxes[n][h]
            if distance < currentSmallestConnection and not wasTheconnectionAlreadyMadev2(tuple(junctionBoxes[h]),tuple(junctionBoxes[n]),connectionsMade):
                connectedBoxes = junctionBoxes[h], junctionBoxes[n]
                currentSmallestConnection = distance
    
    lastSmallestConnection = currentSmallestConnection
    connectionsMade.append({tuple(connectedBoxes[0]), tuple(connectedBoxes[1])})

    indexOfWhereFirstOneIs = -1
    indexOfWhereSecondOneIs = -1

    for k in range(len(connectedJunctionBoxes)):
        if connectedBoxes[0] in connectedJunctionBoxes[k]:
            indexOfWhereFirstOneIs = k
        if connectedBoxes[1] in connectedJunctionBoxes[k]:
            indexOfWhereSecondOneIs = k
    
    if indexOfWhereFirstOneIs == -1 and indexOfWhereSecondOneIs== -1:
        connectedJunctionBoxes.append([connectedBoxes[0],connectedBoxes[1]])
    elif indexOfWhereFirstOneIs == -1:
        connectedJunctionBoxes[indexOfWhereSecondOneIs].append(connectedBoxes[0])
    elif indexOfWhereSecondOneIs == -1:
        connectedJunctionBoxes[indexOfWhereFirstOneIs].append(connectedBoxes[1])
    elif indexOfWhereSecondOneIs != indexOfWhereFirstOneIs: 
        connectedJunctionBoxes[indexOfWhereFirstOneIs] += connectedJunctionBoxes[indexOfWhereSecondOneIs]
        del connectedJunctionBoxes[indexOfWhereSecondOneIs]


lengtsOfJunctions = []

for i in range(len(connectedJunctionBoxes)):
    lengtsOfJunctions.append(len(connectedJunctionBoxes[i]))
                
lengtsOfJunctions.sort()

multiplicationOfbiggest = lengtsOfJunctions[len(lengtsOfJunctions)-1] * lengtsOfJunctions[len(lengtsOfJunctions)-2] * lengtsOfJunctions[len(lengtsOfJunctions)-3]

print(multiplicationOfbiggest)
