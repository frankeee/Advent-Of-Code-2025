lines = []
with open("inputdia3ej1.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.rstrip("\n")) 

maxJoltages = []

#entran y salen ints
def valorMasGrande(empiezaCon,line,tamanio):
    if len(line) < tamanio:
        return False,0
    
    if tamanio == 1:
        return True,int(getMaxValue(line))

    valoresEncontrados = []
    for n in range(len(line)):
        if line[n] == str(empiezaCon):
            existe,valor = valorMasGrande(9,line[n+1:],tamanio - 1)
            if existe:
                valoresEncontrados.append(int(line[n] + str(valor)))
    
    if len(valoresEncontrados) > 0:
        return True, max(valoresEncontrados)
    if empiezaCon > 0:
        return valorMasGrande(empiezaCon - 1,line,tamanio)
    else:
        False,0




def getMaxValue(line):
    maxValue = 0
    for n in line:
        if int(n) > maxValue:
            maxValue = int(n)
    return str(maxValue)

    

for line in lines:
    existe,valor = valorMasGrande(9,line,12)
    if existe:
        maxJoltages.append(valor)
    print("Se proceso una")

print(sum(maxJoltages))

