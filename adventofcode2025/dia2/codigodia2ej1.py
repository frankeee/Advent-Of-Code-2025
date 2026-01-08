with open("inputdia2ej1.txt", "r") as file:
    content = file.read().strip()

# Split by commas and remove empty entries
result = [item for item in content.split(",") if item]

invalidIds = []

ranges = []

for elem in result:
    parts = elem.split("-")
    ranges.append((int(parts[0]),int(parts[1])))


for rangE in ranges:
    for n in range(rangE[0],rangE[1]+1):
        numberAsString = str(n)
        if len(numberAsString) % 2 == 0:
            left = numberAsString[:len(numberAsString)//2]
            right = numberAsString[len(numberAsString)//2:]
            if left == right:
                invalidIds.append(n)
    

print(sum(invalidIds))


