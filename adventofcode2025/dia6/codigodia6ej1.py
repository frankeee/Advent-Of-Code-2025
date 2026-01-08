import operator
completelines = []
with open("C:/Users/FCOL/Documents/adventofcode2025/dia6/inputdia6.txt", "r", encoding="utf-8") as file:
    for line in file:
        completelines.append(line.rstrip("\n"))

results = []

lines = []

for line in completelines:
    linewithoutespacios = []
    digit = ""
    for n in line:
        if n == " ":
            if(len(digit)>0):
                linewithoutespacios.append(digit)
            digit = ""
        else:
            digit += n
    lines.append(linewithoutespacios)



ops = {
    "+": operator.add,
    "*": operator.mul
}

for colNumber in range(len(lines[0])):
    op = lines[len(lines)-1][colNumber]
    result = int(lines[0][colNumber])
    for lineNumber in range(1,len(lines)-1):
        result = ops[op](result, int(lines[lineNumber][colNumber]))
    results.append(int(result))


print(results)
print(sum(results))


