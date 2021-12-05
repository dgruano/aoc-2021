import pandas as pd

def load_data(path:str) -> list:
    data = []
    with open(path) as f:
        for line in f:
            line = line.strip("\n")
            data.append(line)
    return data


def byte_to_int(byte, l:int):
    conv = []
    for i in range(l):
        conv.append(2**i)
    
    num = 0
    for c, v in enumerate(byte[::-1]):
        num += int(v) * conv[c]

    # Instead of inverting byte, I could compute conv as 2 ** (l-1 - i) 
    
    return num


def most_common_bit(data:list) -> int:
    l = len(data[0])
    count = [0] * l
    total = len(data)
    for d in data:
        for c, bit in enumerate(d):
            count[c] += int(bit)  # If bit == 1, it sums. If bit == 0, it sums 0 (so it does not count).
    
    gamma = ""
    epsilon = ""
    for c in count:
        if c > total / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    gamma = byte_to_int(gamma, l)
    epsilon = byte_to_int(epsilon, l)
    return gamma * epsilon


def count_most_common_pos(data:list, pos:int) -> str:
    total = len(data)
    count = 0
    for c, bit in enumerate(data):
        count += int(bit[pos])
    
    if count >= total / 2:
        most_common = "1"
    else:
        most_common = "0"
    
    return most_common


def accepted_data_based_on_pos(data:list, value:str, pos:int) -> list:
    new_data = []
    for d in data:
        if d[pos] == value:
            new_data.append(d)
    
    return new_data


def opposite(bit:str) -> str:
    if bit == "0":
        return "1"
    else:
        return "0"


def most_common_bit_part2(data:list) -> int:
    l = len(data[0])
    total = len(data)
    oxygen = ""
    oxy_data = data
    for i in range(l):
        # Get first digit
        oxygen += count_most_common_pos(oxy_data, i)

        # Rewrite data list with accepted values
        oxy_data = accepted_data_based_on_pos(oxy_data, oxygen[i], i)

        # Calculate total
        total = len(oxy_data)

        # If only one element left, it's the answer
        if total == 1:
            oxygen = oxy_data[0]
            break
    
    # First digit of co2 is the opposite as oxygen
    co2 = opposite(oxygen[0])
    co2_data = accepted_data_based_on_pos(data, co2, 0)
    total = len(co2_data)
    for i in range(1, l):
        co2 += opposite(count_most_common_pos(co2_data, i))

        co2_data = accepted_data_based_on_pos(co2_data, co2[i], i)
                
        # Calculate total
        total = len(co2_data)

        # If only one element left, it's the answer
        if total == 1:
            co2 = co2_data[0]
            break

    oxygen = byte_to_int(oxygen, l)
    co2 = byte_to_int(co2, l)
        
    print(oxygen, co2)
    return oxygen * co2


def most_common_bit_pd(data:list) -> int:
    l = len(data[0])
    df = pd.DataFrame({}, columns = [str(i) for i in range(l)])
    for d in data:
        d = [int(x) for x in d]
        df = df.append(pd.Series(d, index = df.columns), ignore_index=True)
    
    top = df.describe().loc['top']
    bott = (top == False).astype(int)

    oxygen = 0
    co2 = 0

    # Convert bits to int
    for c, bit in enumerate(top[::-1]):
        oxygen += bit * 2**c
        co2 += (not bit) * 2**c
    
    return oxygen * co2


def get_top(s, total):
    if s >= total / 2:
        return 1
    else:
        return 0


def most_common_bit_part2_pd(data:list) -> int:
    l = len(data[0])
    total = len(data)
    df = pd.DataFrame({}, columns = [str(i) for i in range(l)])
    for d in data:
        d = [int(x) for x in d]
        df = df.append(pd.Series(d, index = df.columns), ignore_index=True)
    
    """
    I cannot use df.describe().loc['top'] since it will fail for the special cases
    where the number of 0s and 1s are the same. I will have to do it "manually"
    """
    s = df.sum()
    
    """
    Mathematical expression to substitute an if/else clause
    It is way less legible -see get_top()-, but it was fun to pull it off.
    """ 
    top = s[0] // (total/2) - s[0] // total
    bott = not top  # Save for later

    # Update data to only use entries whose leftmost bit is the MOST frequent
    oxy_df = df.loc[df["0"] == top]
    # Update stats of new data
    s = oxy_df.sum()
    total = len(oxy_df)
    for i in range(1, l):
        print("Index =", i)
        top = s[i] // (total/2) - s[i] // total
        print(top)

        # Update data and stats
        oxy_df = oxy_df.loc[oxy_df[str(i)] == top]
        s = oxy_df.sum()
        total = len(oxy_df)
        
        print(oxy_df)
        print(s)
        print(total)
        print()

        if  total <= 1:
            oxy_byte = oxy_df.sum()  # Filthy way of doing it, but works
            print(oxy_df)
            break
    
    # Update data to only use entries whose leftmost bit is the LEAST frequent
    co2_df = df.loc[df["0"] == bott]
    # Update stats of new data
    s = co2_df.sum()
    total = len(co2_df)
    for i in range(1, l):
        top = s[i] // (total/2) - s[i] // total
        bott = not top  # Get least frequent

        # Update data and stats
        co2_df = co2_df.loc[co2_df[str(i)] == bott]
        s = co2_df.sum()
        total = len(co2_df)

        if total <= 1:
            co2_byte = co2_df.sum()  # Filthy way of doing it, but works
            break
    
    # Convert bits to int
    oxygen = 0
    for c, bit in enumerate(oxy_byte[::-1]):
        oxygen += bit * 2**c

    co2 = 0
    for c, bit in enumerate(co2_byte[::-1]):
        co2 += bit * 2**c

    print(oxygen, co2)

    return oxygen * co2
    

if __name__ == "__main__":
    data = load_data("input.txt")
    result = most_common_bit(data)
    #print(result)

    result = most_common_bit_part2(data)
    print(result)

    data = load_data("input.txt")
    result = most_common_bit_part2_pd(data)
    print(result)