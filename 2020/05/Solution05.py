entries = open("input.txt").read().strip().split("\n")
values = {"F": 0, "B": 1, "L": 0, "R": 1}


def getid(seat):
    return getrow(seat) * 8 + getcolumn(seat)


def getcolumn(seat):
    return getvalue(seat, 9, 6)


def getrow(seat):
    return getvalue(seat, 6, -1)


def getvalue(seat, start, end):
    row = 0
    for i in range(start, end, -1):
        row += values[seat[i]] * 2 ** (start - i)  # * 2 ^ i -> binary -> decimal
    return row


def solve1(lines):
    maximum = 0
    for seat in lines:
        seatid = getid(seat)
        if seatid > maximum:
            maximum = seatid
    print(maximum)


def solve2(lines):
    seats = []
    for seat in lines:
        seatid = getid(seat)
        seats.append(seatid)
    for seatid in seats:
        if seatid + 2 in seats:
            if not seatid + 1 in seats:
                print(str(seatid + 1))
                return
    print("No id found!")


solve1(entries)
solve2(entries)
