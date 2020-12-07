import re

entries = open("input.txt").read().strip().split("\n")
example = open("example.txt").read().strip().split("\n")
eyecolors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def parse(lines):
    passports = []
    passindex = 0
    for line in lines:
        if len(passports) <= passindex:
            passports.append(makePassport())
        passport = passports[passindex]
        if line:  # check if line is empty
            parts = line.split(" ")
            for part in parts:
                split = part.split(":")
                passport[split[0]] = split[1]
        else:
            passindex += 1
    return passports


def makePassport():
    return {'byr': None,
            'iyr': None,
            'eyr': None,
            'hgt': None,
            'hcl': None,
            'ecl': None,
            'pid': None,
            'cid': None}


def solve1(lines):
    count = 0
    passports = parse(lines)
    for passport in passports:
        if isValidPassport1(passport):
            count += 1
            continue
    print(str(count) + " valid passports")


def isValidPassport1(passport):
    for key in passport:
        if passport[key] is None:
            if key != "cid":
                return False
    return True


def solve2(lines):
    count = 0
    passports = parse(lines)
    for passport in passports:
        if isValidPassport2(passport):
            count += 1
            continue
    print(str(count) + " valid passports")


def isValidPassport2(passport):
    if not isValidPassport1(passport):
        return False

    byr = passport["byr"]
    if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
        return False

    iyr = passport["iyr"]
    if len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020:
        return False

    eyr = passport["eyr"]
    if len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030:
        return False

    hgt = passport["hgt"]
    if hgt.endswith("in"):
        height = hgt.replace("in", "")
        if int(height) < 59 or int(height) > 76:
            return False
    elif hgt.endswith("cm"):
        height = hgt.replace("cm", "")
        if int(height) < 150 or int(height) > 193:
            return False
    else:
        return False

    hcl = passport["hcl"]
    if not bool(re.match("^#[0-9a-f]{6}$", hcl)):
        return False

    ecl = passport["ecl"]
    if ecl not in eyecolors:
        return False

    pid = passport["pid"]
    return bool(re.match("^[0-9]{9}$", pid))


solve1(entries)
solve2(entries)
