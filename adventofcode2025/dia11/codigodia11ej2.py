import re
import sys

lines = []

with open("inputdia11.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.rstrip("\n"))

inputoutput = {}
numeroCorrespondienteApalabra = {}
caminosAlFinal =  [[None,None,None,None] for _ in range(len(lines))]
#(completo,dac,fft,llegaalfinal)

for i in range(len(lines)):
    first, rest = lines[i].split(":", 1)
    rest = rest.strip().split()
    inputoutput[first] = rest

    numeroCorrespondienteApalabra[first] = i


def caminosFunc(origen,destino,dac,fft):

    if origen == destino:
        return [0,0,0,1]
    
    numeroCorrepondienteAlOrigen = numeroCorrespondienteApalabra[origen]

    dacEncontrado = False
    fftEncontrado = False

    if origen == dac:
        dacEncontrado = True

    if origen == fft:
        fftEncontrado = True
    
    if caminosAlFinal[numeroCorrepondienteAlOrigen] != [None,None,None,None]:
        return caminosAlFinal[numeroCorrepondienteAlOrigen]
    else:
        caminos = [0,0,0,0]
        #(completo,dac,fft,llegaalfinal)
        for elem in inputoutput[origen]:
            tupla = caminosFunc(elem,destino,dac,fft)

            caminos[0] += tupla[0]

            if dacEncontrado:
                caminos[0] += tupla[2]
                caminos[1] += tupla[3]
                caminos[1] += tupla[1]
            elif fftEncontrado:
                caminos[0] += tupla[1]
                caminos[2] += tupla[3]
                caminos[2] += tupla[2]
            else:
                caminos[1] += tupla[1]
                caminos[2] += tupla[2]
                caminos[3] += tupla[3]

        caminosAlFinal[numeroCorrepondienteAlOrigen] = caminos

        return caminosAlFinal[numeroCorrepondienteAlOrigen]



caminosTotales = caminosFunc("svr","out","dac","fft")
print("se termino caminos")
cantidadTotalDecaminosValidos = caminosTotales[0]



print(cantidadTotalDecaminosValidos)







            

