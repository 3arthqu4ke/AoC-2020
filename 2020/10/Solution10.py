entries = open("input.txt").read().strip().split("\n")
example1 = open("example1.txt").read().strip().split("\n")
example2 = open("example2.txt").read().strip().split("\n")


def convertAdapters(lines):
    sortedLines = [0] + sorted(list(map(int, lines)))
    sortedLines.append(int(sortedLines[len(sortedLines) - 1]) + 3)
    return sortedLines


def solve1(lines):
    converted = convertAdapters(lines)
    jolts = [0, 0]
    for i in range(0, len(converted) - 1):
        diff = int(converted[i + 1]) - int(converted[i])
        if diff == 3:
            jolts[0] += 1
        elif diff == 1:
            jolts[1] += 1
    print("Jolt-1s * Jolt-3s: " + str(jolts[0] * jolts[1]))


def solve2(lines):
    converted = convertAdapters(lines)
    values = [1]
    for i in range(0, len(converted) - 1):
        values.append(0)
    for i in range(0, len(converted)):
        adapter = converted[i]
        for j in range(i - 3, i):
            if adapter - converted[j] < 4:
                values[i] += values[j]
    print("Permutations: " + str(values[len(values) - 1]))


solve1(entries)
solve2(entries)
