players = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
games = {}
x = 0
for i1 in range(len(players)-3):
	for i2 in range(i1 + 1, len(players)-2):
		for i3 in range(i2 + 1, len(players) - 1):
			for i4 in range(i3 + 1, len(players)):
				x += 1
				games[x] = [players[i1], players[i2], players[i3], players[i4]]


def crossnumbers(list1, list2):
	result = 0
	for i in list1:
		if i in list2:
			result += 1
	return result

part = {}
collector = set()
gamestodelete = []
for i in games:
	if set(games[i]).isdisjoint(collector):
		collector.update(set(games[i]))
		part[i] = games[i]
		gamestodelete.append(i)

for i in gamestodelete:
	games.pop(i)
gamestodelete = []
print(collector)
print(part)

pairs = set()
for i1 in range(len(players)-1):
	for i2 in range(i1 + 1, len(players)):
		a = tuple([i1, i2])
		pairs.add(a)
print(pairs)
