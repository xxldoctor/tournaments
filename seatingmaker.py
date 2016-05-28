from random import shuffle


def makingpart(part, players, j):
	for i in seating:
		part[i + 20 * j] = [players[seating[i][0]], players[seating[i][1]], players[seating[i][2]], players[seating[i][3]]]
	return part


def gameslist(part, games):
	for i in players1:
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


def makeplayers(playerslist):
	players = {
		'A': 'Андрей',  # 'Андрей Ланцов',
		'B': 'Юл',  # 'Юлия Логинова',
		'C': 'Зайчик',  # 'Дмитрий Зайчиков',
		'D': 'Сергей',  # 'Сергей Мазаев',
		'E': 'Женя',  # 'Евгения Нетребина',
		'F': 'Лена',  # 'Елена Фадина',
		'G': 'Влад',  # 'Влад Мамин',
		'H': 'Наташа',  # 'Наталья Долгушина',
		'I': 'Мико',  # 'Александр Невзоров',
		'J': 'Док',  # 'Кирилл Хромов',
		'K': 'Оля',  # 'Ольга Алексеева',
		'L': 'Леон',  # 'Леон Николаев',
		'M': 'Дима',  # 'Дмитрий Быков',
		'N': 'Миша',  # 'Михаил Петухов',
		'O': 'Митя',  # 'Дмитрий Новиков',
		'P': 'Антон',  # 'Антон Новиков'
	}
	result = []
	for i in playerslist:
		result.append(players[i])
	return result


seating = {
	1: [0, 1, 2, 3],
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
	20: [3, 4, 10, 13]
}

playerslist1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
playerslist2 = ['B', 'J', 'G', 'K', 'C', 'D', 'E', 'O', 'H', 'A', 'N', 'F', 'L', 'P', 'I', 'M']
playerslist3 = ['O', 'K', 'P', 'B', 'A', 'D', 'F', 'E', 'L', 'I', 'M', 'N', 'C', 'G', 'J', 'H']
players1 = makeplayers(playerslist1)
players2 = makeplayers(playerslist2)
players3 = makeplayers(playerslist3)
part = {}
games = {}
for z in players1:
	games[z] = []
makingpart(part, players1, 0)
makingpart(part, players2, 1)
makingpart(part, players3, 2)
gameslist(part, games)

print('первый список:', players1)
print('второй список:', players2)
print('третий список:', players3)

print()
for j in players1:
	print('Ханчаны игрока ' + j + ':')
	for i in games[j]:
		print(str(i) + ': [' + part[i][0] + ' ' + part[i][1] + ' ' + part[i][2] + ' ' + part[i][3] + ']')
	print()

print()
for i in range(1, 61):
	print('Ханчан №' + str(i) + ': [' + part[i][0] + ' ' + part[i][1] + ' ' + part[i][2] + ' ' + part[i][3] + ']')
