
def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    patterns = {}
    stats = []

    i = 0
    # --- Parse patterns ---
    while i < len(lines):
        line = lines[i].strip()

        # Stop if we reached the stats section
        if ":" in line and "x" in line:
            break

        # Pattern header like "0:"
        if line.endswith(":") and line[:-1].isdigit():
            pattern_id = int(line[:-1])
            i += 1

            grid = []
            # Read following non-empty grid lines
            while i < len(lines) and lines[i].strip() != "":
                grid.append(lines[i])
                i += 1

            patterns[pattern_id] = grid

        i += 1

    # --- Parse stats ---
    while i < len(lines):
        line = lines[i].strip()
        if line:
            stats.append(line)
        i += 1

    return patterns, stats
def parse_stat_line(line):
    # Example input: "4x4: 0 0 0 0 2 0"
    size_part, values_part = line.split(":")
    
    base_str, height_str = size_part.split("x")
    base = int(base_str)
    height = int(height_str)

    numbers = list(map(int, values_part.strip().split()))

    return base, height, numbers

# Example usage:
patterns, stats = read_file("inputdia12.txt")

requirements = []

for s in stats:
    parsed_stat = parse_stat_line(s)
    requirement = {}
    requirement["base"] = parsed_stat[0]
    requirement["height"] = parsed_stat[1]
    requirement["listOfRequiredShapes"] = parsed_stat[2]
    requirements.append(requirement)


patternsAsLists = []

for k in patterns:
    patternsAsLists.append(patterns[k])

shapes = []
for p in patternsAsLists:
    shape = {}
    shape["shape_size"] = 0
    for line in p:
        shape["shape_size"] += line.count("#")
    shape["dimension"] = p
    shapes.append(shape)


countOfPossibles = 0

for requirement in requirements:
    maxValue = requirement["base"] * requirement["height"]
    valorTotal = 0
    for n in range(len(requirement["listOfRequiredShapes"])):
        valorParaEstaShape = requirement["listOfRequiredShapes"][n] * shapes[n]["shape_size"]
        valorTotal += valorParaEstaShape
    
    if valorTotal <= maxValue:
        countOfPossibles+=1

print(countOfPossibles)




    



            

