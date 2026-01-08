section1 = []
section2 = []
current = section1

with open(
    "C:/Users/Franco/Documents/adventofcode2025/dia5/inputdia5.txt",
    "r",
    encoding="utf-8"
) as file:
    for line in file:
        line = line.rstrip("\n")

        if line == "":
            current = section2
            continue

        current.append(line)

ranges = section1
itemsAsStrings = section2

rangesAsTupleOfStrings = []
rangesAsTuple = []
items = []

for range in ranges:
    left, right = range.split("-")
    rangesAsTupleOfStrings.append((left, right))

for range in rangesAsTupleOfStrings:
    lower = int(range[0])
    upper = int(range[1])
    rangesAsTuple.append((lower, upper))

for item in itemsAsStrings:
    items.append(int(item))


availableFreshIngredients = 0

for item in items:
    for range in rangesAsTuple:
        if range[0] <= item and item <= range [1]:
            availableFreshIngredients += 1
            break

print(availableFreshIngredients)


