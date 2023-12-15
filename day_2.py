day = 2

with open(f"Inputs/day{day}.txt") as f:
    lines = f.read().splitlines()

# Part 1
test=[
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
]

sol = []
for line in lines:
    bag = {'red': 0, 'green': 0, 'blue': 0}
    game,rest = line.split(': ')
    game = int(game.split(' ')[1])
    pulled = ', '.join(rest.split('; ')).split(', ')
    for p in pulled:
        count, color = p.split(' ')
        bag[color] = max(bag[color],int(count))
    if bag['red'] <= 12 and bag['green'] <= 13 and bag['blue'] <= 14:
        sol.append(game)

print('part1', sum(sol))

# Part 2

test=[
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
]

sol = []
for line in lines:
    bag = {'red': 0, 'green': 0, 'blue': 0}
    game,rest = line.split(': ')
    game = int(game.split(' ')[1])
    pulled = ', '.join(rest.split('; ')).split(', ')
    for p in pulled:
        count, color = p.split(' ')
        bag[color] = max(bag[color],int(count))
    
    power = bag['red'] * bag['green'] * bag['blue']
    sol.append(power)
    


print('part2', sum(sol))