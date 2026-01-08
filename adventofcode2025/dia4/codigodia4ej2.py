lines = []
with open("C:/Users/Franco/Documents/adventofcode2025/dia4/inputdia4.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.rstrip("\n"))

def numberOfAdjacentRolls(lines, numerofila, numerocol):
    numeroDeRollosAdyacentes= 0
    desdeFila = 0
    hastaFila = 0
    desdeCol = 0
    hastaCol = 0

    if numerofila == 0:
        desdeFila = numerofila
        hastaFila = numerofila + 1
    elif numerofila == len(lines) - 1:
        desdeFila = numerofila - 1
        hastaFila = numerofila
    else:
        desdeFila = numerofila - 1
        hastaFila = numerofila + 1
    
    if numerocol == 0:
        desdeCol = numerocol
        hastaCol = numerocol + 1
    elif numerocol == len(lines[numerofila]) - 1:
        desdeCol = numerocol - 1
        hastaCol = numerocol
    else:
        desdeCol = numerocol - 1
        hastaCol = numerocol + 1

    for posicionFila in range(desdeFila,hastaFila + 1):
        for posicionColumna in range(desdeCol,hastaCol + 1):
            if lines[posicionFila][posicionColumna] == "@":
                numeroDeRollosAdyacentes +=1
    
    return numeroDeRollosAdyacentes - 1



numberOfAccesibleRolls = 0
rollsareremoved = True
while rollsareremoved:
    numberOfRollsRemoved = 0
    for lineNumber in range(len(lines)):
        for position in range(len(lines[lineNumber])):
            if lines[lineNumber][position] == "@":
                if numberOfAdjacentRolls(lines,lineNumber,position) < 4:
                    numberOfAccesibleRolls += 1
                    numberOfRollsRemoved += 1
                    lines[lineNumber] = lines[lineNumber][:position] + "." + lines[lineNumber][position + 1:]
    
    if numberOfRollsRemoved == 0:
        rollsareremoved = False

print(numberOfAccesibleRolls)

