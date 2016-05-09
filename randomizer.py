from random import shuffle


def makingpart(players):
	part = {}
	for i in seating:
		part[i] = [players[seating[i][0]], players[seating[i][1]], players[seating[i][2]], players[seating[i][3]]]
	return part


def gameslist(part, games):
	for i in players1:
		games[i] = []
		for game in part:
			if i in part[game]:
				games[i].append(game)
	return games


def fucksgiven(cpart1, cpart2):
	fucks = {3: 0, 4: 0}
	for i in range(1, 21):
		for j in range(1, 21):
			n = 0
			for x in range(4):
				if cpart1[i][x] in cpart2[j]:
					n += 1
			if n > 2:
				fucks[n] += 1
	return fucks


def generateplayers(players):
	shuffle(players)
	newpart = (makingpart(players))
	return newpart


seating = {1: [0, 1, 2, 3],
		   2: [4, 5, 6, 7],
		   3: [8, 9, 10, 11],
		   4: [12, 13, 14, 15],
		   5: [0, 4, 8, 12],
		   6: [1, 5, 9, 13],
		   7: [2, 6, 10, 14],
		   8: [3, 7, 11, 15],
		   9: [0, 5, 10, 15],
		   10: [1, 4, 11, 14],
		   11: [2, 7, 8, 13],
		   12: [3, 6, 9, 12],
		   13: [0, 6, 11, 13],
		   14: [1, 7, 10, 12],
		   15: [2, 4, 9, 15],
		   16: [3, 5, 8, 14],
		   17: [0, 7, 9, 14],
		   18: [1, 6, 8, 15],
		   19: [2, 5, 11, 12],
		   20: [3, 4, 10, 13]}

players1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
# players2 = ['K', 'G', 'D', 'N', 'E', 'P', 'I', 'M', 'C', 'A', 'J', 'F', 'B', 'O', 'L', 'H']
# players3 = ['C', 'K', 'D', 'N', 'E', 'O', 'L', 'F', 'M', 'B', 'H', 'I', 'J', 'G', 'P', 'A']
games1 = {}
games2 = {}
games3 = {}
part1 = makingpart(players1)
gameslist(part1, games1)

players2 = list(players1)
fails = {3: 0, 4: 1}
while (fails[3] > 0) or (fails[4] > 0):
	part2 = generateplayers(players2)
	fails = fucksgiven(part1, part2)
gameslist(part2, games2)

players3 = list(players1)
fails1 = {3: 0, 4: 1}
fails2 = {3: 0, 4: 1}
while (fails1[3] > 0) or (fails1[4] > 0) or (fails2[3] > 4) or (fails2[4] > 0):
	part3 = generateplayers(players3)
	fails1 = fucksgiven(part1, part3)
	fails2 = fucksgiven(part2, part3)
gameslist(part3, games3)

print(players1)
print(players2)
print(players3)
print('1 to 2:')
print(fucksgiven(part1, part2))
print('1 to 3:')
print(fucksgiven(part1, part3))
print('2 to 3:')
print(fucksgiven(part2, part3))

print('1st')
print(part1)
print(games1)
print('2nd')
print(part2)
print(games2)
print('3rd')
print(part3)
print(games3)
