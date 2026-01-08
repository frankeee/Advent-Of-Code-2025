lines = []
with open("inputdia1ej1.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.rstrip("\n"))  # remove trailing newline

#print(lines)

ceroCounter = 0
initialNumber = 50

def getLetterFromLine(line):
    return line[0]

def getNumberFromLine(line):
    numbersAsLetters = line[1:]
    return int(numbersAsLetters)

def applysumToNumber(initialNumber,sum,ceroCounter):
    for _ in range(sum):
        if initialNumber == 99 :
            initialNumber = 0
        else:
            initialNumber += 1
        if initialNumber == 0:
            ceroCounter+= 1
    return initialNumber,ceroCounter

def applysubstractionToNumber(initialNumber,substraction,ceroCounter):
    for _ in range(substraction):
        if initialNumber == 0:
            initialNumber = 99
        else:
            initialNumber -= 1
        if initialNumber == 0:
            ceroCounter+= 1
    return initialNumber,ceroCounter


for line in lines:
    numberToApply = getNumberFromLine(line)
    if getLetterFromLine(line) == "R":
        initialNumber,ceroCounter = applysumToNumber(initialNumber,numberToApply,ceroCounter)
    elif getLetterFromLine(line) == "L":
        initialNumber,ceroCounter = applysubstractionToNumber(initialNumber,numberToApply,ceroCounter)
    

print(ceroCounter)
