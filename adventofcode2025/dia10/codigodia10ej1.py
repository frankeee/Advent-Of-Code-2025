import re
import sys

lines = []

with open("C:/Users/Franco/Documents/adventofcode2025/dia10/inputdia10.txt", "r", encoding="utf-8") as file:
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
    switchesToTurnOn = element[0][0]
    targetSwitches = set()
    for n in range(len(switchesToTurnOn)):
        if switchesToTurnOn[n] == "#":
            targetSwitches.add(n)

    buttons = []
    for n in range(len(element[1])):
        button = set()
        for h in element[1][n]:
            if h != ",":
                button.add(int(h))
        buttons.append(button)
    
    orderedElectricStuff.append([targetSwitches,buttons])

def generateListsOfPossibleButtonPresses(listOfPressedButtons):

    if len(listOfPressedButtons) == 1:
        return [[0], [1]]

    result = []

    del listOfPressedButtons[0]

    listsToComplete = generateListsOfPossibleButtonPresses(listOfPressedButtons)

    for list in listsToComplete:
        list0 = [0] + list
        result.append(list0)

        list1 = [1] + list
        result.append(list1)

    return result
        
listOfButtonPresses = []

for element in orderedElectricStuff:
    keepgoing = True
    targetButtons = element[0]
    buttons = element[1]
    #aca va a haber que optimizarlo para que haya un contador desde 1 pero teniendo en cuenta que no van a ser mas de len(buttons)
    listsOfPossibleButtonPresses = generateListsOfPossibleButtonPresses([0] * len(buttons))
    minButtonPresses = sys.maxsize
    for list in listsOfPossibleButtonPresses:
        if sum(list) < minButtonPresses:
            copyOfTargetButtons = targetButtons
            for n in range(len(list)):
                if list[n] == 1:
                    copyOfTargetButtons = copyOfTargetButtons ^ buttons[n]
            
            if len(copyOfTargetButtons) == 0:
                minButtonPresses = sum(list)
    
    listOfButtonPresses.append(minButtonPresses)

print(sum(listOfButtonPresses))







            

