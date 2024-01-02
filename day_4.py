day = 4

with open(f"Inputs/day{day}.txt") as f:
    lines = f.read().splitlines()

test = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']
# lines = test
# part 1
points = 0
for line in lines:
    card, nums = line.split(' | ')
    card = card.split(': ')[1].split(' ')
    nums = nums.split(' ')
    card = filter(lambda x: x , card)
    nums = filter(lambda x: x , nums)
    winners = list(set(card) & set(nums))
    if len(winners) == 1:
        points+=1
    elif len(winners) > 1:
        points+= pow(2,len(winners)-1)

print('part1', points)

# part 2
card_map = {}
for i in range(1, len(lines) + 1):
    card_map[str(i)] = 1

for i in range(1, len(lines) + 1):
    copies = card_map[str(i)]

for line in lines:
    card, nums = line.split(' | ')
    card_num, card = card.split(': ')
    card_num = card_num.split(' ')[-1]
    card = card.split(' ')
    nums = nums.split(' ')
    card = filter(lambda x: x , card)
    nums = filter(lambda x: x , nums)
    num_winners = len(list(set(card) & set(nums)))
    count = card_map[card_num]
    for i in range(1, num_winners + 1):
        card_map[str(int(card_num) + i)] += count

cards = list(map(lambda x: int(x), card_map.values()))

print('part2', sum(cards))