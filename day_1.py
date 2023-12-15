day = 1

with open(f"Inputs/day{day}.txt") as f:
    lines = f.read().splitlines()


# Part 1
test = ['1abc2',
'pqr3stu8vwx',
'a1b2c3d4e5f',
'treb7uchet']

nums = 0
for line in lines:
    f = next(filter(lambda x: x.isdigit(), line))
    l = next(filter(lambda x: x.isdigit(), reversed(line)))
    num = int(f+l)
    nums += num

print('part1', nums)

# Part 2

test = ['two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen']

digits = 'one two three four five six seven eight nine'.split()
intMap = {}
for i in range(1,10):
    intMap[digits[i-1]] = str(i)

digits += [str(d) for d in range(1,10)]

def foo(s, findingLast):
    smallest = len(s)
    num = None
    for d in digits:
        if findingLast and not d.isdigit():
            d = d[::-1]
        index = s.find(d)
        if index < smallest and index != -1:
            smallest = index
            if findingLast and not d.isdigit():
                d = d[::-1]
            num = d
    return num

nums = 0
for line in lines:
    f = foo(line, False)
    f = f if f.isdigit() else intMap[f]
    l = foo(line[::-1], True)
    l = l if l.isdigit() else intMap[l]
    num = int(f+l)
    nums += num

print('part2', nums)
