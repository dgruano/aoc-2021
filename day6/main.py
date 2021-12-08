import numpy as np

def load_data(path:str) -> np.ndarray:
    with open(path, "r") as f:
        data = f.readlines()[0]
        data = data.split(",")
    data = np.asarray(data, dtype=np.int64)
    return data


def get_lanternfish_growth(data:np.ndarray, days:int) -> int:
    for _ in range(days):
        # Reduce all counters
        data = data - 1

        # Check negatives
        parents = data == -1
        count_parents = sum(parents)

        # Reset parents and create newborns
        data[parents] = 6
        data = np.append(data, [8] * count_parents)

        # You must NEVER EVER append iteratively to an array if you want to be efficient.
        # If you want to keep your house warm using your RAM, it could be an idea...

    total = len(data)
    return total


def get_lanternfish_counters(data, days):
    # Each value in this list contains the number of fish
    # in the phase corresponding to the index
    counters = np.asarray([0] * 9, dtype=np.int64)
    for fish in data:
        counters[fish] += 1

    for _ in range(days):
        # Reduce one day (shift all counters to the left)
        counters = np.roll(counters, -1)

        # Each dividing fish gives a child (position 8, or last position)
        # but also stays alive and continues cycling (add to position 6)
        parents = counters[-1]
        counters[6] += parents

    return sum(counters)


if __name__ == "__main__":
    data = load_data("input.txt")
    print(get_lanternfish_counters(data, days=80))
    #print(get_lanternfish_growth(data, days=256))  # Run this if you want to see the world burn
    print(get_lanternfish_counters(data, days=256))
