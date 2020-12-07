entries = open("input.txt").read().strip().split("\n")


def convert(line):  # regex...
    s = line.split("-")
    minimum = s[0]
    s = s[1].split(" ")
    maximum = s[0]
    letter = str(s[1]).replace(":", "")
    word = s[2]
    return [minimum, maximum, letter, word]


def checkAll(lines):
    count = 0
    for line in lines:
        s = convert(line)
        if checkPassword(s[0], s[1], s[2], s[3]):
            count += 1
    print(str(count) + " lines are valid by Definition1")


def checkPassword(minimum, maximum, letter, word):
    count = 0
    for c in word:
        if c == letter:
            count += 1
    if count < int(minimum) or count > int(maximum):
        return False
    return True


def checkAll2(lines):
    count = 0
    for line in lines:
        s = convert(line)
        if checkPassword2(s[0], s[1], s[2], s[3]):
            count += 1
    print(str(count) + " lines are valid by Definition2")


def checkPassword2(first, second, letter, word):
    f = word[int(first) - 1]  # Toboggan Corporate Policies have no concept of "index zero"!
    s = word[int(second) - 1]
    if s == letter and f != letter or s != letter and f == letter:
        return True
    return False


checkAll(entries)
checkAll2(entries)
