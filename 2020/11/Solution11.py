entries = open("input.txt").read().strip().split("\n")


grid = [[None for x in range(len(entries[0]))] for y in range(len(entries))]
for c, row in enumerate(entries):
    for i, word in enumerate(row):
        # noinspection PyTypeChecker
        grid[c][i] = str(word)


def solve(lines, func, maxocc):
    current = lines.copy()
    while True:
        last = current
        current = takeASeat(last, [[None for x in range(len(entries[0]))] for y in range(len(entries))], func, maxocc)
        if last == current:
            break
    count = 0
    for y in current:
        for x in y:
            if x == '#':
                count += 1
    print("Occupied Seats: " + str(count) + ".")


def takeASeat(seats, newseats, neighbourfunc, maxocc):
    for y, line in enumerate(seats):
        for x, seat in enumerate(line):
            newseats[y][x] = getNewOccupation(seats[y][x], x, y, seats, line, neighbourfunc, maxocc)
    return newseats


def getNewOccupation(letter, x, y, seats, line, neighbourfunc, mynameismaximumoccupancyonehundredandtwenty):
    count = 0
    for neighbour in neighbourfunc(x, y, seats, line):
        seat = seats[y + neighbour[1]][x + neighbour[0]]
        if seat == '#':
            count += 1
    if letter == 'L' and count == 0:
        return '#'
    if letter == '#' and count >= mynameismaximumoccupancyonehundredandtwenty:
        return 'L'
    return letter


# AHHH
def neighbourFunc1(x, y, seats, line):
    result = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    if x == 0:
        remove(result, [-1, 0])
        remove(result, [-1, 1])
        remove(result, [-1, -1])
    if y == 0:
        remove(result, [0, -1])
        remove(result, [1, -1])
        remove(result, [-1, -1])
    if x == len(line) - 1:
        remove(result, [1, 0])
        remove(result, [1, -1])
        remove(result, [1, 1])
    if y == len(seats) - 1:
        remove(result, [1, 1])
        remove(result, [-1, 1])
        remove(result, [0, 1])
    return result


def neighbourFunc2(x, y, seats, line):
    result = []
    for neighbour in neighbourFunc1(x, y, seats, line):
        xLimit = -2 if neighbour[0] == 0 else (0 if neighbour[0] < 0 else len(line) - 1)
        yLimit = -2 if neighbour[1] == 0 else (0 if neighbour[1] < 0 else len(seats) - 1)
        nX = neighbour[0]
        nY = neighbour[1]
        while seats[y + nY][x + nX] == "." and x + nX != xLimit and y + nY != yLimit:
            nX += neighbour[0]
            nY += neighbour[1]
        if seats[y + nY][x + nX] != ".":
            result.append([nX, nY])
    return result


def remove(elements, element):
    if element in elements:
        elements.remove(element)


solve(grid, lambda x, y, seats, line: neighbourFunc1(x, y, seats, line), 4)
solve(grid, lambda x, y, seats, line: neighbourFunc2(x, y, seats, line), 5)
