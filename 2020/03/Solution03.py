entries = open("input.txt").read().strip().split("\n")
example = ["..##.......",
           "#...#...#..",
           ".#....#..#.",
           "..#.#...#.#",
           ".#...##..#.",
           "..#.##.....",
           ".#.#.#....#",
           ".#........#",
           "#.##...#...",
           "#...##....#",
           ".#..#...#.#"]


def solve1(lines):
    index = 0
    count = 0
    for line in lines:
        while len(line) <= index:  # concatenate if too short
            line += line
        if line[index] == "#":
            count += 1
        index += 3
    print(count)


def solve2(lines):
    result = solveSlope(lines, 1, 1)
    result *= solveSlope(lines, 3, 1)
    result *= solveSlope(lines, 5, 1)
    result *= solveSlope(lines, 7, 1)
    result *= solveSlope(lines, 1, 2)
    print(result)


def solveSlope(lines, right, down):
    r = 0
    d = 0
    count = 0
    while d < len(lines):
        line = lines[d]
        while len(line) <= r:  # concatenate if too short
            line += line
        if line[r] == "#":
            count += 1
        r += right
        d += down
    return count


solve1(entries)
solve2(entries)

