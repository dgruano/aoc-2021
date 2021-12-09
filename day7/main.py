import itertools
import numpy as np


def load_data(path:str) -> list:
    with open(path, "r") as f:
        data = f.readlines()[0]
        data = data.split(",")
        data = [int(x) for x in data]
    return data


def optimize_crab_fuel(positions:list) -> int:
    # Create map:
    # index will be the position
    ## value will be the fuel needed to go to that position
    n_crabs = len(positions)
    max_pos = max(positions)
    ocean = np.zeros((n_crabs, max_pos))

    for c, pos in enumerate(positions):
        move_left = list(range(pos))[::-1]  # Same as list(range(pos-1, -1, -1))
        stay = []
        move_right = list(range(1, max_pos - pos + 1))
        moving_range = move_left + stay + move_right

        # Add moving range to the current position of the crab
        ocean[c,:] = moving_range

    return int(min(np.sum(ocean, 0)))


def optimize_crab_fuel_incremental(positions:list) -> int:
    # Create map:
    # index will be the position
    # value will be the fuel needed to go to that position
    n_crabs = len(positions)
    max_pos = max(positions)
    ocean = np.zeros((n_crabs, max_pos))

    for c, pos in enumerate(positions):

        move_left = list(itertools.accumulate(range(0, pos)))[::-1]
        stay = []
        move_right = list(itertools.accumulate(range(1, max_pos - pos + 1, 1)))
        moving_range = move_left + stay + move_right

        # Add moving range to the current position of the crab
        ocean[c,:] = moving_range

    return int(min(np.sum(ocean, 0)))



if __name__ == "__main__":
    #data = load_data("input.txt")
    data = load_data("test_input.txt")
    print(optimize_crab_fuel(data))

    data = load_data("input.txt")
    print(optimize_crab_fuel_incremental(data))
