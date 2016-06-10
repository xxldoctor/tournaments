def crossnumbers(list1, list2):
	result = 0
	for i in list1:
		if i in list2:
			result += 1
	return result


def partmaker(games):
	collector = set()
	part = {}
	gamestodelete = []
	for i in games:
		if set(games[i]).isdisjoint(collector):
			collector.update(set(games[i]))
			part[i] = games[i]
			gamestodelete.append(i)
	gamescleaner(games, gamestodelete)
	return part

def gamescleaner(games, deletelist):
	for i in deletelist:
		games.pop(i)
	return

# pairs = set()
# for i1 in range(len(players)-1):
# 	for i2 in range(i1 + 1, len(players)):
# 		a = tuple([i1, i2])
# 		pairs.add(a)
# print(pairs)


players = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
games = {}
x = 0
for i1 in range(len(players)-3):
	for i2 in range(i1 + 1, len(players)-2):
		for i3 in range(i2 + 1, len(players) - 1):
			for i4 in range(i3 + 1, len(players)):
				x += 1
				games[x] = [players[i1], players[i2], players[i3], players[i4]]
# print(games)
gamessessions = []
for i in range(2):
	gamessessions.append(partmaker(games))
	print(gamessessions[i])
# print(games)
