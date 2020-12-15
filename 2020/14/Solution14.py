entries = open("input.txt").read().strip().split("\n")


def solve(lines, maskfunc):
    memory, mask = {}, None
    for i, split in enumerate([x.split(" ") for x in lines]):
        if split[0] == "mask":
            mask = split[2]
        else:
            maskfunc(memory, split[0], mask, int(split[2]))
    print(sum(memory.values()))


def applyMask1(memory, addr, mask, number):
    nullMask, realMask = "", ""
    for char in mask:
        nullMask += "1" if char == "X" else "0"
        realMask += "1" if char == "1" else "0"
    memory[addr] = (number & int(nullMask, 2)) | int(realMask, 2)


solve(entries, lambda mem, addr, mask, num: applyMask1(mem, addr, mask, num))
