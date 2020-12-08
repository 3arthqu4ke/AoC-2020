entries = open("input.txt").read().strip().split("\n")


def solve1(lines, printout=True):
    accumulator = 0
    checked = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if i in checked:
            if printout:
                print(str(accumulator) + ", infinite loop.")
            return "True " + str(accumulator)  # added for 2nd part
        checked.append(i)
        if "acc" in line:
            accumulator += int(line.strip().split(" ")[1])
        elif "jmp" in line:
            i += int(line.strip().split(" ")[1])
            continue
        i += 1
    if printout:
        print("No infinite loop.")
    return "False " + str(accumulator)  # added for 2nd part


def solve2(lines):
    current = lines
    operation = -1
    lastOp = -1
    while solve1(current, False).split(" ")[0] != "False":
        operation = -1
        current = []
        for i in range(0, len(lines)):
            line = lines[i]
            if operation == -1 and i > lastOp:
                if "nop" in line:
                    operation = i
                    current.append("jmp " + line.split(" ")[1])
                    print(current[i])
                    continue
                if "jmp" in line:
                    operation = i
                    current.append("nop " + line.split(" ")[1])
                    print(current[i])
                    continue
            current.append(line)
        lastOp = operation
    print(solve1(current, False).split(" ")[1] + ", no infinite loop. (" + str(operation) + ")")


solve1(entries)
solve2(entries)
