section1 = []
section2 = []
current = section1

with open(
    "C:/Users/Franco/Documents/adventofcode2025/dia5/inputdia5.txt",
    "r",
    encoding="utf-8"
) as file:
    for line in file:
        line = line.rstrip("\n")

        if line == "":
            current = section2
            continue

        current.append(line)

ranges = section1
itemsAsStrings = section2

rangesAsTupleOfStrings = []
rangesAsTuple = []
items = []

for pepe in ranges:
    left, right = pepe.split("-")
    rangesAsTupleOfStrings.append((left, right))

for peper in rangesAsTupleOfStrings:
    lower = int(peper[0])
    upper = int(peper[1])
    rangesAsTuple.append((lower, upper))

for item in itemsAsStrings:
    items.append(int(item))

def isContained(specificRange,availableFreshIngredients):
    for item in availableFreshIngredients:
        if item[0] <= specificRange[0] and specificRange[1] <= item[1]:
            return True
    return False

def areExtensible(newRange,otherspecificrange):
    if newRange[0] == otherspecificrange[0] and newRange[1] == otherspecificrange[1] or isContained(otherspecificrange,[newRange]):
        return False

    if newRange[1] <= otherspecificrange[1]:
        if not newRange[1] < otherspecificrange[0]:
            return True
        return False
    
    if otherspecificrange[1] <= newRange[1]:
        if not otherspecificrange[1] < newRange[0]:
            return True
        return False

availableFreshIngredients = []

for specificrange in rangesAsTuple:
    if not isContained(specificrange,availableFreshIngredients):
        newRange = [0,0]
        newRange[0] = specificrange[0]
        newRange[1] = specificrange[1]
        wasChangedAgain = True
        while wasChangedAgain:
            wasItChanged = False
            
            for otherspecificrange in rangesAsTuple:
                if areExtensible(newRange,otherspecificrange):
                    newRange[0] = min(newRange[0],otherspecificrange[0])
                    newRange[1] = max(newRange[1],otherspecificrange[1])
                    wasItChanged = True
            wasChangedAgain = wasItChanged
        availableFreshIngredients.append(newRange)
    
sumaDeIngredientes = 0

for ingredientes in availableFreshIngredients:
    sumaDeIngredientes+= ingredientes[1] - ingredientes[0] + 1

print(sumaDeIngredientes)


