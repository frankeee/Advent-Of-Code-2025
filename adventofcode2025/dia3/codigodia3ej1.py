def getSecondDigit(h,line):
    maxValue = 0
    for n in range(h,len(line)):
        if int(line[n]) > maxValue:
            maxValue = int(line[n])
    return maxValue

lines = []
with open("inputdia3ej1.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.rstrip("\n")) 

maxJoltages = []

for line in lines:
    maxJoltage = 0
    for n in range(10): #hay que chequear esto
        firstDigit = 9 - n
        for h in range(len(line)):
            if int(line[h]) == firstDigit and h != len(line) - 1:
                secondDigit = getSecondDigit(h+1,line)
                if maxJoltage < int(str(firstDigit)+ str(secondDigit)):
                    maxJoltage = int(str(firstDigit)+ str(secondDigit))
    maxJoltages.append(maxJoltage)

print(sum(maxJoltages))

