lines = []
with open("C:/Users/Franco/Documents/adventofcode2025/dia7/inputdia7.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.rstrip("\n"))


def timesThatWillBeSplit(lines, positionOfTachion):
    
    if positionOfTachion[0] == len(lines) - 1:
        matrix[positionOfTachion[0]][positionOfTachion[1]] = 1
        return matrix[positionOfTachion[0]][positionOfTachion[1]]
    
    if matrix[positionOfTachion[0]][positionOfTachion[1]] != None:
        return matrix[positionOfTachion[0]][positionOfTachion[1]]
    
    if lines[positionOfTachion[0]][positionOfTachion[1]] == ".":
        matrix[positionOfTachion[0]][positionOfTachion[1]] = timesThatWillBeSplit(lines, (positionOfTachion[0] + 1, positionOfTachion[1]))
        return matrix[positionOfTachion[0]][positionOfTachion[1]]
    
    if lines[positionOfTachion[0]][positionOfTachion[1]] == "^":
        matrix[positionOfTachion[0]][positionOfTachion[1]] = timesThatWillBeSplit(lines, (positionOfTachion[0], positionOfTachion[1] + 1)) + timesThatWillBeSplit(lines, (positionOfTachion[0], positionOfTachion[1] - 1))
        return matrix[positionOfTachion[0]][positionOfTachion[1]]

positionOfS = 0,0

for n in range(len(lines)):
    for i in range(len(lines[n])):
        if lines[n][i] == "S":
            positionOfS = n,i

matrix = [[None for _ in range(len(lines[0]))] for _ in range(len(lines))]

result = timesThatWillBeSplit(lines, (positionOfS[0] + 1, positionOfS[1]))

print(result)


