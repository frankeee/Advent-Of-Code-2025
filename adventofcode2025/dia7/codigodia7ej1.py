lines = []
with open("C:/Users/Franco/Documents/adventofcode2025/dia7/inputdia7.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.rstrip("\n"))


def timesThatWillBeSplit(lines, positionOfTachion, activatedSplitters):

    if positionOfTachion[0] == len(lines) - 1:
        return activatedSplitters
    
    if positionOfTachion in activatedSplitters:
        return activatedSplitters
    
    if lines[positionOfTachion[0]][positionOfTachion[1]] == ".":
        return timesThatWillBeSplit(lines, (positionOfTachion[0] + 1, positionOfTachion[1]), activatedSplitters)
    
    if lines[positionOfTachion[0]][positionOfTachion[1]] == "^":
        activatedSplitters.add((positionOfTachion[0],positionOfTachion[1]))
        return timesThatWillBeSplit(lines, (positionOfTachion[0], positionOfTachion[1] + 1), activatedSplitters).union(timesThatWillBeSplit(lines, (positionOfTachion[0], positionOfTachion[1] - 1), activatedSplitters))

positionOfS = 0,0

for n in range(len(lines)):
    for i in range(len(lines[n])):
        if lines[n][i] == "S":
            positionOfS = n,i


result = len(timesThatWillBeSplit(lines, (positionOfS[0] + 1, positionOfS[1]), set()))

print(result)


