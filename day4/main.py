import re
import numpy as np


def load_data(path:str) -> tuple[list, list]:
    with open(path, "r") as f:
        # Initialize storing variables
        boards = []
        b = []

        for c, line in enumerate(f):
            line = line.strip("\n ")

            if c == 0:
                # First line, read order of numbers
                bingo = line.split(",")
                bingo = [int(x) for x in bingo]

            else:
                # Board lines
                if not line:
                    if b:
                        boards.append(np.asarray(b, dtype=np.int64))
                        b = []

                else:
                    line = re.split(" +", line)
                    b.append(line)

        # Add last board
        boards.append(np.asarray(b, dtype=np.int64))

    return bingo, boards


def is_winner(mask:np.ndarray) -> bool:
    for x in range(5):
        if sum(mask[x,:]) == 5 or sum(mask[:,x]) == 5:
            # Bingo
            return True

    return False


def get_winner_board(bingo:list, boards:list) -> int:
    # Initialize the masks that contain marked numbers
    masks = []
    for a in range(len(boards)):
        # Important to declare dtype. Masks with non-bool values have different behaviour
        masks.append(np.reshape(np.asarray([0]*25, dtype=np.bool8), (5,5)))

    # Iterate through the number draws
    for c, n in enumerate(bingo):
        # Iterate through boards and mark drawn number
        for i, b in enumerate(boards):
            masks[i][b == n] = 1  # Could also use DataFrame.mask()

            # Check winner
            if is_winner(masks[i]):
                # Declare winner variables for clarity
                winner_mask = masks[i]
                winner_board = b
                last_number = n
                break

        else:
            continue

        # Break outer loop if inner loop was broken
        break

    winner_sum = sum(sum(winner_board * ~winner_mask))
    return winner_sum * last_number


def get_loser_board(bingo:list, boards:list) -> int:
    # Initialize the masks that contain marked numbers
    masks = []
    has_won = [False] * len(boards)
    for _ in range(len(boards)):
        # Important to declare dtype. Masks with non-bool values have different behaviour
        masks.append(np.reshape(np.asarray([0]*25, dtype=np.bool8), (5,5)))

    # Iterate through the number draws
    for c, n in enumerate(bingo):
        # Iterate through boards and mark drawn number
        for i, b in enumerate(boards):
            masks[i][b == n] = 1  # Could also use DataFrame.mask()

            # Check winner
            if is_winner(masks[i]):
                has_won[i] = True
                if not False in has_won:
                    # All boards have won, last one is the loser
                    # Declare loser variables for clarity
                    loser_board = b
                    loser_mask = masks[i]
                    last_number = n
                    break

            else:
                continue

        else:
            continue

        # Break outer loop if inner loop was broken
        break

    winner_sum = sum(sum(loser_board * ~loser_mask))
    return winner_sum * last_number


if __name__ == "__main__":
    bingo, boards = load_data("input.txt")
    print(get_winner_board(bingo, boards))
    print(get_loser_board(bingo, boards))
