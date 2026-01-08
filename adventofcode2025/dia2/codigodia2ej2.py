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
        #print(numberAsString)
        for waysToSplit in range(2,len(numberAsString)+1):
            if len(numberAsString) % waysToSplit == 0:
                sizeOfChunks = len(numberAsString) // waysToSplit
                chunks = []
                for h in range(0,len(numberAsString),sizeOfChunks):
                    chunks.append(numberAsString[h:h + sizeOfChunks])
                #print(chunks)
                if len(set(chunks)) == 1:
                    invalidIds.append(n)
                    break
    

print(sum(invalidIds))


