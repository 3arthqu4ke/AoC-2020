entries = open("input.txt").read().strip().split("\n")
timestamp = int(entries[0])
buses = ["x" if x == "x" else int(x) for x in entries[1].split(",")]


def solve1(time, busids):
    mindist, minid = float("inf"), -1
    for busid in busids:
        if busid != "x":
            distance = 0
            while distance < time:
                distance += busid
            if distance - time < mindist :
                mindist, minid = distance - time, busid
    print("Fastest bus * minutes is: " + str(minid * mindist))


def solve2(busids):
    modulos = {bus: -i % bus for i, bus in enumerate(busids) if bus != "x"}
    sort = list(reversed(sorted(modulos)))
    result = modulos[sort[0]]
    offset = sort[0]
    for entry in sort[1:]:
        while result % entry != modulos[entry]:
            result += offset
        offset *= entry
    print("First TimeStamp: " + str(result))


solve1(timestamp, buses)
solve2(buses)
