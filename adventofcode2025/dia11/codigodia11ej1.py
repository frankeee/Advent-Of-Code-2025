import re
import sys

lines = []

with open("inputdia11.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.rstrip("\n"))

inputoutput = {}
numeroCorrespondienteApalabra = {}
caminosAlFinal =  [None for _ in range(len(lines))]

for i in range(len(lines)):
    first, rest = lines[i].split(":", 1)
    rest = rest.strip().split()
    inputoutput[first] = rest

    numeroCorrespondienteApalabra[first] = i


def cantidadDeCaminosDesde(origen,destino):
    if origen == destino:
        return 1
    
    numeroCorrepondienteAlOrigen = numeroCorrespondienteApalabra[origen]

    if caminosAlFinal[numeroCorrepondienteAlOrigen] != None:
        return caminosAlFinal[numeroCorrepondienteAlOrigen]
    else:
        cantidadDeCaminos = 0
        for elem in inputoutput[origen]:
            cantidadDeCaminos+= cantidadDeCaminosDesde(elem,destino)
        
        caminosAlFinal[numeroCorrepondienteAlOrigen] = cantidadDeCaminos

        return cantidadDeCaminos



cantidadDeCaminosTotales = cantidadDeCaminosDesde("you","out")


print(cantidadDeCaminosTotales)







            

