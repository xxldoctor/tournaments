# Список игроков:
# Андрей Юл Зайчик Леон // Зайчик - Дмитрий Зайчиков
# Мико Лена Оля Наташа // Мико - Александр Невзоров
# Женя Док Влад Сергей // Док - Кирилл Хромов
# Дима Миша Митя Антон // Митя - Дмитрий Новиков

people = list(input().split(";"))
peoplelist = []
for i in people:
	peoplelist.append(set(i.split()))

part = {
	1: {'Андрей', 'Юл', 'Зайчик', 'Сергей'},
	# 2: {'Женя', 'Лена', 'Влад', 'Наташа'},
	3: {'Мико', 'Док', 'Оля', 'Леон'},
	4: {'Дима', 'Миша', 'Митя', 'Антон'},
	5: {'Андрей', 'Женя', 'Мико', 'Дима'},
	# 6: {'Юл', 'Лена', 'Док', 'Миша'},
	# 7: {'Зайчик', 'Влад', 'Оля', 'Митя'},
	# 8: {'Сергей', 'Наташа', 'Леон', 'Антон'},
	9: {'Андрей', 'Лена', 'Оля', 'Антон'},
	# 10: {'Юл', 'Женя', 'Леон', 'Митя'},
	11: {'Зайчик', 'Наташа', 'Мико', 'Миша'},
	# 12: {'Сергей', 'Влад', 'Док', 'Дима'},
	# 13: {'Андрей', 'Влад', 'Леон', 'Миша'},
	# 14: {'Юл', 'Наташа', 'Оля', 'Дима'},
	15: {'Зайчик', 'Женя', 'Док', 'Антон'},
	# 16: {'Сергей', 'Лена', 'Мико', 'Митя'},
	# 17: {'Андрей', 'Наташа', 'Док', 'Митя'},
	18: {'Юл', 'Влад', 'Мико', 'Антон'},
	# 19: {'Зайчик', 'Лена', 'Леон', 'Дима'},
	# 20: {'Сергей', 'Женя', 'Оля', 'Миша'},
	# 21: {'Юл', 'Док', 'Влад', 'Оля'},
	# 22: {'Зайчик', 'Сергей', 'Женя', 'Митя'},
	# 23: {'Наташа', 'Андрей', 'Миша', 'Лена'},
	24: {'Леон', 'Антон', 'Мико', 'Дима'},
	25: {'Юл', 'Зайчик', 'Наташа', 'Леон'},
	# 26: {'Док', 'Сергей', 'Андрей', 'Антон'},
	# 27: {'Влад', 'Женя', 'Миша', 'Мико'},
	# 28: {'Оля', 'Митя', 'Лена', 'Дима'},
	29: {'Юл', 'Сергей', 'Миша', 'Дима'},
	30: {'Док', 'Зайчик', 'Лена', 'Мико'},
	31: {'Влад', 'Митя', 'Наташа', 'Антон'},
	# 32: {'Оля', 'Женя', 'Андрей', 'Леон'},
	33: {'Юл', 'Женя', 'Лена', 'Антон'},
	34: {'Док', 'Митя', 'Миша', 'Леон'},
	35: {'Влад', 'Зайчик', 'Андрей', 'Дима'},
	# 36: {'Оля', 'Сергей', 'Наташа', 'Мико'},
	# 37: {'Юл', 'Митя', 'Андрей', 'Мико'},
	38: {'Док', 'Женя', 'Наташа', 'Дима'},
	# 39: {'Влад', 'Сергей', 'Лена', 'Леон'},
	# 40: {'Оля', 'Зайчик', 'Миша', 'Антон'},
	# 41: {'Митя', 'Оля', 'Антон', 'Юл'},
	# 42: {'Андрей', 'Сергей', 'Лена', 'Женя'},
	43: {'Леон', 'Мико', 'Дима', 'Миша'},
	# 44: {'Зайчик', 'Влад', 'Док', 'Наташа'},
	45: {'Митя', 'Андрей', 'Леон', 'Зайчик'},
	46: {'Оля', 'Сергей', 'Мико', 'Влад'},
	47: {'Антон', 'Лена', 'Дима', 'Док'},
	# 48: {'Юл', 'Женя', 'Миша', 'Наташа'},
	49: {'Митя', 'Сергей', 'Дима', 'Наташа'},
	# 50: {'Оля', 'Андрей', 'Миша', 'Док'},
	# 51: {'Антон', 'Женя', 'Леон', 'Влад'},
	52: {'Юл', 'Лена', 'Мико', 'Зайчик'},
	# 53: {'Митя', 'Лена', 'Миша', 'Влад'},
	54: {'Оля', 'Женя', 'Дима', 'Зайчик'},
	55: {'Антон', 'Андрей', 'Мико', 'Наташа'},
	56: {'Юл', 'Сергей', 'Леон', 'Док'},
	# 57: {'Митя', 'Женя', 'Мико', 'Док'},
	58: {'Оля', 'Лена', 'Леон', 'Наташа'},
	59: {'Антон', 'Сергей', 'Миша', 'Зайчик'},
	60: {'Юл', 'Андрей', 'Дима', 'Влад'}
}


for group in peoplelist:
	posgames = set()
	players = set()
	for i in part:
		if ((len(group) < 4) and (group.issubset(part[i]))) or ((len(group) >= 4) and (part[i].issubset(group))):
			posgames.add(i)
			players.update(part[i])
	for i in posgames:
		print(i, part[i])
	group.difference_update(players)
	print('нужные игроки: ' + str(players))
	print('могут не идти: ' + str(group))
	print()
