entries = open("input.txt").read().strip().split("\n")
cachedPermutations = {0: {}, 1: {"0", "1"}}
maskPermutations = {}
memory = {}


def solve(lines):
    lastMask, maskIndex = None, []
    for i, split in enumerate([x.split(" ") for x in lines]):
        if split[0] == "mask":
            lastMask = split[2]
            for perm in cachePermutations(split[2]):
                maskPerm, index = "", 0
                for j, char in enumerate(split[2]):
                    if char == "X":
                        maskPerm += str(int(perm[index]) + 5)
                        index += 1
                        continue
                    maskPerm += char
                if lastMask not in maskPermutations:
                    maskPermutations[lastMask] = [maskPerm]
                else:
                    maskPermutations[lastMask].append(maskPerm)
        maskIndex.append(lastMask)
    for i, split in enumerate(list(reversed([x.split(" ") for x in lines]))):
        lastMask = maskIndex[len(lines) - i - 1]
        if split[0] != "mask":
            binAddr = bin(int(split[0].replace("mem[", "").replace("]", ""))).replace("0b", "")
            binAddr = [char for char in "0" * (36 - len(binAddr)) + binAddr]
            for maskPerm in maskPermutations[lastMask]:
                address = ""
                for j, char in enumerate(maskPerm):
                    if char == "0":
                        address += binAddr[j]
                    elif char == "1":
                        address += "1"
                    else:
                        address += str(int(char) - 5)
                if address not in memory:
                    print(split[0], address[25:38])
                    memory[address] = int(split[2])
    print(sum(memory.values()))


def cachePermutations(address):
    arrayPermutations, count = [], address.count("X")
    if count in cachedPermutations:
        arrayPermutations = cachedPermutations[count]
    else:
        flag = False
        if count == 9:
            flag = True
            print("Caching 9X permutations, this will take a second...")
        for i in range(0, count + 1):
            arrayPermutations += permutate([1] * i + [0] * (count - i))
        cachedPermutations[count] = set(arrayPermutations)
        if flag:
            print("Cached 9X.")
    return set(arrayPermutations)


def permutate(array):
    out = []
    if len(array) < 2:
        return array
    else:
        for i, entry in enumerate(array):
            for perm in permutate(array[:i] + array[i + 1:]):
                out += [str(entry) + str(perm)]
    return out


solve(entries)
