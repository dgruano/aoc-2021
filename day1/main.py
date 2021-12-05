def load_data(path:str) -> list:
    data = []
    with open(path) as f:
        for line in f:
            line = line.strip("\n")
            line = int(line)
            data.append(line)
    return data


def count_larger_than_previous(data:list) -> int:
    count = 0
    for c, item in enumerate(data):
        if item > data[c-1]:
            count += 1
    return count


def count_larger_than_previous_window(data:list, size:int) -> int:
    count = 0
    prev_sum = sum(data[0:3])
    for c, _ in enumerate(data[1: 1-size], start = 1):
        new_sum = sum(data[c: c+3])
        if new_sum > prev_sum:
            count += 1

        prev_sum = new_sum

    return count


def count_larger_than_previous_window_opt(data:list, size:int) -> int:
    count = 0
    first = data[0]
    prev_sum = sum(data[0:3])  # Sum of first window
    new_sum = 0
    for c, item in enumerate(data[1: 1-size], start=1):
        new_sum = prev_sum - first + data[c+2]
        if new_sum > prev_sum:
            count += 1

        first = item  # Measurement that disappears of the window next iteration
    
    return count
    



if __name__ == '__main__':
    data = load_data("input.txt")
    result = count_larger_than_previous(data)
    print(result)

    result2 = count_larger_than_previous_window(data, 3)
    print(result2)

    result3 = count_larger_than_previous_window_opt(data, 3)
    print(result3)