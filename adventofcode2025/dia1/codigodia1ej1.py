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

def applysumToNumber(initialNumber,sum):
    for _ in range(sum):
        if initialNumber == 99 :
            initialNumber = 0
        else:
            initialNumber += 1
    return initialNumber

def applysubstractionToNumber(initialNumber,substraction):
    for _ in range(substraction):
        if initialNumber == 0:
            initialNumber = 99
        else:
            initialNumber -= 1
    return initialNumber


for line in lines:
    numberToApply = getNumberFromLine(line)
    if getLetterFromLine(line) == "R":
        initialNumber = applysumToNumber(initialNumber,numberToApply)
    elif getLetterFromLine(line) == "L":
        initialNumber = applysubstractionToNumber(initialNumber,numberToApply)
    if initialNumber == 0:
        ceroCounter += 1

print(ceroCounter)
