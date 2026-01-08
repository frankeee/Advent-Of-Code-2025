import re
from z3 import *

lines = []

with open("C:/Users/FCOL/Documents/adventofcode2025/dia10/inputdia10.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.rstrip("\n"))

electricStuff = []

for line in lines:
    square_brackets = re.findall(r"\[([^\]]+)\]", line)
    parentheses = re.findall(r"\(([^)]+)\)", line)
    curly_brackets = re.findall(r"\{([^}]+)\}", line)
    electricStuff.append([square_brackets,parentheses,curly_brackets])

orderedElectricStuff = []

for element in electricStuff:
    
    buttons = []
    for n in range(len(element[1])):
        button = set()
        parts = element[1][n].split(",")
        for h in parts:
            button.add(int(h))
        buttons.append(button)

    targetJoltages = []
    parts = element[2][0].split(",")
    for n in parts:
        targetJoltages.append(int(n))
    
    orderedElectricStuff.append([buttons,targetJoltages])


listOfButtonPresses = []
counterOfElems = 0
for element in orderedElectricStuff:

    counterOfElems+=1
    print("vamos " + str(counterOfElems) + " de " + str(len(orderedElectricStuff)))

    buttons = element[0]
    targetJoltages = element[1]

    opt = Optimize()

    buttonsForZ3 = [Int(f'button_{i}') for i in range(len(buttons))]

    for b in buttonsForZ3:
        opt.add(b >= 0)

    for i in range(len(targetJoltages)):
        indices = []
        for h in range(len(buttons)):
            for item in buttons[h]:
                if item == i:
                    indices.append(h)
                    break

        opt.add(Sum(buttonsForZ3[j] for j in indices) == targetJoltages[i])
    
    total_presses = Sum(buttonsForZ3)

    opt.minimize(total_presses)

    if opt.check() == sat:
        model = opt.model()
        listOfButtonPresses.append(model.evaluate(total_presses).as_long())



print(listOfButtonPresses)
print(sum(listOfButtonPresses))



    



   








            

