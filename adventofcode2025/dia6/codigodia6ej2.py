import operator
completelines = []
with open("C:/Users/FCOL/Documents/adventofcode2025/dia6/inputdia6.txt", "r", encoding="utf-8") as file:
    for line in file:
        completelines.append(line.rstrip("\n"))


symbolPositions = []

for n in range(len(completelines[len(completelines)-1])):
    if completelines[len(completelines)-1][n] != " ":
        symbolPositions.append(n)


lines  = []
for completeline in completelines:
    line = []
    for n in range(len(symbolPositions)):
        if n != len(symbolPositions) - 1:
            line.append(completeline[symbolPositions[n]:symbolPositions[n+1]-1])
        else:
            line.append(completeline[symbolPositions[n]:len(completeline)-1])
    lines.append(line)

valuesToOperateOn = []

for colNumber in range(len(lines[0])):
    OrderedNumbers = [""] * len(lines[0][colNumber])
    for rowNumber in range(len(lines)-1):
        for n in range(len(lines[rowNumber][colNumber])):
            if lines[rowNumber][colNumber][n] != " ":
                OrderedNumbers[n] += lines[rowNumber][colNumber][n]
    OrderedNumbers.append(lines[len(lines)-1][colNumber][0])
    valuesToOperateOn.append(OrderedNumbers)

ops = {
    "+": operator.add,
    "*": operator.mul
}

results = []

for values in valuesToOperateOn:
    acumulator = 0
    op = values[len(values)-1]
    if op == "*":
        acumulator = 1
    for n in range(len(values)-1):
        acumulator = ops[op](acumulator,int(values[n]))
    results.append(acumulator)
        

print(sum(results))


