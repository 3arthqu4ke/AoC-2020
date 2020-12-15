puzzle = [11, 18, 0, 20, 1, 7, 16]


def solve(lines, number):
    first, spoken, last = False, {}, 0
    for i in range(0, number):
        before = last
        if i < len(lines):
            spoken[lines[i]] = i
            if i == len(lines) - 1:
                first = True
            last = lines[i]
        else:
            if first:
                last = 0
                first = False
            else:
                last = i - spoken[last]
        if last not in spoken:
            first = True
        spoken[before] = i
    print(str(number) + "th number: " + str(last))


solve(puzzle, 2020)
solve(puzzle, 30000000)  # wont think about a better one
