import numpy as np

def load_data(path:str) -> list:
    data = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip("\n")
            line = line.split(" -> ")
            line = [x.split(",") for x in line]
            data.append(line)
    return data


def get_crossing_points(data:list, l:int=1000, simple:bool=False) -> int:

    # Create ocean map with side lenght = l
    ocean = np.zeros((l,l))

    for d in data:
        x1 = int(d[0][0])
        y1 = int(d[0][1])
        x2 = int(d[1][0])
        y2 = int(d[1][1])


        # Filter out diagonals if simple mode
        if simple and x1 != x2 and y1 != y2:
            ##print("Diagonal", d)
            # Diagonal line
            continue

        # Get individual coordinates of points in the line
        if x1 < x2:  # (0,5) (2,1)
            dir_x = list(range(x1, x2 + 1))
        elif x1 > x2:
            dir_x = list(range(x1, x2 - 1, -1))
        else:
            # Vertical line
            # Add same x coordinate as many times as the distance between y2 and y1 + 1
            dir_x = [x1] * (abs(y2 - y1) + 1)

        if y1 < y2:
            dir_y = list(range(y1, y2 + 1))
        elif y1 > y2:
            dir_y = list(range(y1, y2 - 1, -1))
        else:
            # Horizontal line
            # Add same y coordinate as many times as the distance between x2 and x1 + 1
            dir_y = [y1] * (abs(x2 - x1) + 1)

        for i, xi in enumerate(dir_x):
            ocean[dir_y[i], xi] += 1

    # Count points were 2 or more lines cross
    count = sum(sum(ocean >= 2))
    return count


if __name__ == "__main__":
    data = load_data("input.txt")

    print(get_crossing_points(data, simple=True))

    print(get_crossing_points(data))
