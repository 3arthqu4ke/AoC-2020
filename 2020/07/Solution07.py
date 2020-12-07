import re

entries = open("input.txt").read().strip().split("\n")
bags = {}

#  AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH


def parserules(lines):
    bags.clear()
    for rule in lines:
        bagcolor = rule.split("bags")[0].strip()
        if bagcolor not in bags:
            bags[bagcolor] = []
        rules = re.findall("[0-9]+[a-zA-Z ]+bag", rule)
        for r in rules:
            r = r.replace(" bag", "")
            amounts = re.findall("[0-9]+", r)
            if len(amounts) == 0:
                continue
            color = re.split("[0-9]+", r)[1]
            for i in range(0, int(amounts[0])):
                bags[bagcolor].append(color.strip())


def solve(lines):
    parserules(lines)
    count = 0
    for bag in bags.keys():
        if checkBag(bag):
            count += 1
    print(count)

# contained was unnecessary until we changed parserules method to add multiple bags


def checkBag(bag, contained=None):
    if contained is None:
        contained = []
        # in case shiny gold one can contain shiny gold ones
        if bag == "shiny gold":
            return checkbags(bag, contained)
    if bag == "shiny gold":
        return True
    if bag in contained:
        return False
    contained.append(bag)
    return checkbags(bag, contained)


def checkbags(bag, contained):
    if bag not in bags:
        return False
    for bag1 in bags[bag]:
        if checkBag(bag1, contained):
            return True
    return False


def solve2(lines):
    parserules(lines)
    print(getbagcount("shiny gold"))


def getbagcount(bag, checked=None):
    if checked is None:
        checked = {}
    if len(bags[bag]) == 0:
        checked[bag] = 0
        return 0
    if bag not in checked:
        count = 0
        for bag1 in bags[bag]:
            count += getbagcount(bag1, checked) + 1
        checked[bag] = count
    return checked[bag]


solve(entries)
solve2(entries)
