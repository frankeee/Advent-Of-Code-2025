import re
import sys

lines = []

with open("C:/Users/Franco/Documents/adventofcode2025/dia10/inputdia10.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.rstrip("\n"))

def generateListsOfPossibleButtonPresses(i,listOfPressedButtons,JoltageThatLimitsMaxTimesButtonsCanBePressed,WhichButtonsActivateEachJoltage):
    
    if i == len(buttons):
        return [listOfPressedButtons]

    result = []

    elem = buttons[i]

    buttonPressesLeft = targetJoltages[JoltageThatLimitsMaxTimesButtonsCanBePressed[i]]

    for elem in WhichButtonsActivateEachJoltage[JoltageThatLimitsMaxTimesButtonsCanBePressed[i]]:
        if elem < i:
            buttonPressesLeft -= listOfPressedButtons[elem]

    buttonPressesLeft = max(buttonPressesLeft,0)

    for n in range(0,buttonPressesLeft+1):

        new_list = listOfPressedButtons.copy()
        new_list.append(n)
    
        listsToComplete = generateListsOfPossibleButtonPresses(i+1,new_list,JoltageThatLimitsMaxTimesButtonsCanBePressed,WhichButtonsActivateEachJoltage)

        for list1 in listsToComplete:
            result.append(list1)

    return result    

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

    JoltageThatLimitsMaxTimesButtonsCanBePressed = []
    
    for button in buttons:
        minForButton = sys.maxsize
        whichJoltage = None
        for item in button:
            if targetJoltages[item] < minForButton:
                minForButton = targetJoltages[item]
                whichJoltage = item
        JoltageThatLimitsMaxTimesButtonsCanBePressed.append(whichJoltage)
    
    WhichButtonsActivateEachJoltage = [set() for _ in range(len(targetJoltages))]

    for h in range(len(buttons)):
        for item in buttons[h]:
            WhichButtonsActivateEachJoltage[item].add(h)

    possibleLists = generateListsOfPossibleButtonPresses(0,[],JoltageThatLimitsMaxTimesButtonsCanBePressed,WhichButtonsActivateEachJoltage)

    minButtonPresses = sys.maxsize
    
    for possiblelist in possibleLists:
        print(possiblelist)
        if sum(possiblelist) < minButtonPresses:
            joltagesForThisList = [0] * len(targetJoltages)
            for n in range(len(possiblelist)):
                for item in buttons[n]:
                    joltagesForThisList[item]+=1 * possiblelist[n]
                
            if joltagesForThisList == targetJoltages:
                minButtonPresses = sum(possiblelist)
            
    listOfButtonPresses.append(minButtonPresses)

print(listOfButtonPresses)   



    



   








            

