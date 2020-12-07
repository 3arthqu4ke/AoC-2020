entries = open("input.txt").read().strip().split("\n")


# meh this could definitely be cleaned up
# but this is the last one before Im up to date
def solve1(lines):
    groups = []
    index = 0
    for line in lines:
        if len(groups) <= index:
            groups.append({})
        group = groups[index]
        if line:
            for c in line:
                group[c] = c
        else:
            index += 1
    count = 0
    for group in groups:
        count += len(group)
    print(count)


def solve2(lines):
    groups = []
    index = 0
    groupsize = 0
    for line in lines:
        if len(groups) <= index:
            groups.append({})
        group = groups[index]
        if line:
            groupsize += 1
            for c in line:
                group[c] = group.get(c, 0) + 1
        else:
            group["size"] = groupsize
            groupsize = 0
            index += 1
            continue
        group["size"] = groupsize
    count = 0
    for group in groups:
        for q in group.keys():
            if q == "size":
                continue
            if group[q] == group["size"]:
                count += 1
    print(count)


solve1(entries)
solve2(entries)
