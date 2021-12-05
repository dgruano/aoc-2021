def load_data(path:str) -> list:
    data = []
    with open(path) as f:
        for line in f:
            line = line.strip("\n")
            line = line.split(" ")
            line[1] = int(line[1])
            data.append(line)
    return data


def calculate_coordinates(data:list) -> int:
    horizontal = 0
    depth = 0
    for command in data:
        if command[0] == "forward":
            horizontal += command[1]
        if command[0] == "down":
            depth += command[1]
        if command[0] == "up":
            depth -= command[1]
        
        if depth < 0:
            depth = 0
    
    return horizontal*depth


def calculate_coordinates_part2(data:list) -> int:
    horizontal = 0
    depth = 0  # Should not be negative ?
    aim = 0  # Could be negative (submarine facing up)

    for command in data:
        if command[0] == "forward":
            horizontal += command[1]
            depth += aim * command[1]
        if command[0] == "down":
            aim += command[1]
        if command[0] == "up":
            aim -= command[1]

    return horizontal*depth

if __name__ == "__main__":
    data = load_data("day2/input.txt")
    result = calculate_coordinates(data)
    print(result)

    data = load_data("day2/input.txt")
    result = calculate_coordinates_part2(data)
    print(result)