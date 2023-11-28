def can_transform(start, end):
    i, j = 0, 0

    while i < len(start) and j < len(end):
        while i < len(start) and start[i] == 'X':
            i += 1
        while j < len(end) and end[j] == 'X':
            j += 1

        if (i < len(start) and j == len(end)) or (i == len(start) and j < len(end)):
            return False

        if i < len(start) and j < len(end):
            if start[i] != end[j]:
                return False
            elif start[i] == 'L' and i < j:
                return False
            elif start[i] == 'R' and i > j:
                return False

        i += 1
        j += 1

    return True

# Example usage for Exercise-1
result1 = can_transform("RXXLRXRXL", "XRLXXRRLX")
print(result1)
