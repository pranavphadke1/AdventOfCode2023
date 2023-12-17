day = 3

with open(f"Inputs/day{day}.txt") as f:
    lines = f.read().splitlines()

import re
# part 1

test = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
]

# lines = test
answer = 0
numbers = []
for y in range(len(lines)):
    line = lines[y]
    indices = [(match.start(), match.group()) for match in re.finditer(r'\d+', line)]
    for x, num in indices:
        numbers.append((x,y, num))

def getVal(pair, num):
    x_coord,y_coord = pair
    c = lines[y_coord][x_coord]
    if c != '.' and not c.isdigit():
        return int(num)

def shouldAdd(num):
    x, y, num = num
    line = lines[y]
    top_left = (x - 1, y -1) if x>0 and y>0 else None
    top_right = (x + len(num), y -1) if x + len(num) < len(line) and y > 0 else None
    bottom_left = (x - 1, y + 1) if x>0 and y + 1<len(lines) else None
    bottom_right = (x + len(num), y + 1) if x + len(num) < len(line) and y + 1<len(lines) else None
    corners = [top_left, top_right, bottom_left, bottom_right]
    
    # Check the four corners
    for corner in corners:
        if not corner:
            continue
        val = getVal(corner, num)
        if val: return val
        
    # Check left
    left = (x-1, y) if x > 0 else None
    if left:
        val = getVal(left, num)
        if val: return val
    # Check right
    right = (x+len(num), y) if x+len(num) < len(line) else None
    if right:
        val = getVal(right, num)
        if val: return val
    # Check top and bottom of number
    for i in range (len(num)):
        # cur index on number substring
        j = x + i
        top = (j, y -1) if y > 0 else None
        bot = (j, y + 1) if y + 1 < len(lines) else None
        if top:
            val = getVal(top, num)
            if val: return val
        if bot:
            val =  getVal(bot, num)
            if val: return val
    return False

for n in numbers:
    num = shouldAdd(n)
    if num: answer += num

print('part1', answer)

# part 2

answer = 0
numbers = []
for y in range(len(lines)):
    line = lines[y]
    indices = [(match.start(), match.group()) for match in re.finditer(r'\d+', line)]
    for x, num in indices:
        numbers.append((x,y, num))

def getVal(pair, num):
    x_coord,y_coord = pair
    c = lines[y_coord][x_coord]
    if c != '.' and not c.isdigit():
        return int(num)

gearMap = {}

def addToMap(num, val):
    if num in gearMap:
        gearMap[num].append(val)
    else:
        gearMap[num] = [val]

def findGears(num):
    x, y, num = num
    line = lines[y]
    top_left = (x - 1, y -1) if x>0 and y>0 else None
    top_right = (x + len(num), y -1) if x + len(num) < len(line) and y > 0 else None
    bottom_left = (x - 1, y + 1) if x>0 and y + 1<len(lines) else None
    bottom_right = (x + len(num), y + 1) if x + len(num) < len(line) and y + 1<len(lines) else None
    corners = [top_left, top_right, bottom_left, bottom_right]
    
    # Check the four corners
    for corner in corners:
        if not corner:
            continue
        val = getVal(corner, num)
        if val: addToMap(corner, val)
        
    # Check left
    left = (x-1, y) if x > 0 else None
    if left:
        val = getVal(left, num)
        if val: addToMap(left, val)
    # Check right
    right = (x+len(num), y) if x+len(num) < len(line) else None
    if right:
        val = getVal(right, num)
        if val: addToMap(right, val)
    # Check top and bottom of number
    for i in range (len(num)):
        # cur index on number substring
        j = x + i
        top = (j, y -1) if y > 0 else None
        bot = (j, y + 1) if y + 1 < len(lines) else None
        if top:
            val = getVal(top, num)
            if val: addToMap(top, val)
        if bot:
            val =  getVal(bot, num)
            if val: addToMap(bot, val)

for n in numbers:
    findGears(n)

for val in gearMap.values():
    if len(val) == 2:
        part1, part2 = val
        answer += part1 * part2

print('part2', answer)