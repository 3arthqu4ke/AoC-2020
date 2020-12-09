entries = open("input.txt").read().strip().split("\n")


def solve1(lines):
    for i in range(25, len(lines)):
        if not check(i, lines):
            print("Its " + lines[i] + " in line " + str(i) + ".")
            return i
    print("No line found!")
    return 0


def check(index, lines):
    number = int(lines[index])
    for i in range(index - 25, index):
        for j in range(index - 25, index):
            if i == j:
                continue
            if int(lines[i]) + int(lines[j]) == number:
                return True
    return False


def solve2(lines):
    number = int(lines[solve1(lines)])
    for i in range(0, len(lines)):
        ints = [int(lines[i])]
        for j in range(i + 1, len(lines)):
            ints.append(int(lines[j]))
            if sum(ints) > number:
                break
            if sum(ints) == number:
                print(str(min(ints) + max(ints)) + ", from lines " + str(i) + "-" + str(j) + ".")
                return
    print("No numbers found!")


solve2(entries)
