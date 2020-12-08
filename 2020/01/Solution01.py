example = [1721, 979, 366, 299, 675, 1456]
numbers = [int(i) for i in open("inputs.txt").read().strip().split("\n")]


def solve1(entries):
    for i in range(0, len(entries)):
        num = entries[i]
        for j in range(0, len(entries)):
            if i == j:  # case 1010 ?
                continue
            other = entries[j]
            if other + num == 2020:
                printresults([num, other])
                return
    print("No Results found...")


def solve2(entries):
    for i in range(0, len(entries)):
        num = entries[i]
        for j in range(0, len(entries)):
            if i == j:
                continue
            other = entries[j]
            for k in range(0, len(entries)):
                if i == k or j == k:
                    continue
                other2 = entries[k]
                if num + other + other2 == 2020:
                    printresults([num, other, other2])
                    return
    print("No Results found...")


def printresults(results):
    result = 1
    for i in results:
        print(i)
        result *= i
    print(str(result) + " multiplied")


solve1(numbers)
print()
solve2(numbers)
