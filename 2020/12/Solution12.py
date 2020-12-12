entries = [[str(a[:1]), int(a[1:])] for a in open("input.txt").read().strip().split("\n")]
vecs = {"N": [0, 1, 0], "E": [1, 0, 0], "W": [-1, 0, 0], "S": [0, -1, 0], "L": [0, 0, -1], "R": [0, 0, 1]}
translate = {0: "N", 90: "E", 180: "S", 270: "W"}


def solve1(lines):
    x, y, look = 0, 0, 90
    for ins in lines:
        vector = vecs[translate[look % 360]] if ins[0] == "F" else vecs[ins[0]]
        x, y, look = x + vector[0] * ins[1], y + vector[1] * ins[1], look + vector[2] * ins[1]
    print("1.) Manhattan distance: " + str(abs(x) + abs(y)))


def solve2(lines):
    wX, wY, x, y = 10, 1, 0, 0
    for ins in lines:
        if ins[0] == "F":
            x, y = x + wX * ins[1], y + wY * ins[1]
        elif ins[0] == "R" or ins[0] == "L":
            xFac = 1 if ins[0] == "R" else -1
            for i in range(0, ins[1] // 90):
                wX, wY = wY * xFac, wX * xFac * -1
        else:
            wX, wY = wX + vecs[ins[0]][0] * ins[1], wY + vecs[ins[0]][1] * ins[1]
    print("2.) Manhattan distance: " + str(abs(x) + abs(y)))


solve1(entries)
solve2(entries)
