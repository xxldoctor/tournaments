people = {'Андрей Ланцов', 'Юлия Логинова', 'Дмитрий Зайчиков', 'Сергей Мазаев', 'Евгения Нетребина', 'Елена Фадина',
		  'Александр Невзоров'}
games = {'Ольга Алексеева': [3, 7, 9, 14, 20, 21, 28, 32, 36, 40, 41, 46, 50, 54, 58],
		 'Александр Невзоров': [3, 5, 11, 16, 18, 24, 27, 30, 36, 37, 43, 46, 52, 55, 57],
		 'Евгения Нетребина': [2, 5, 10, 15, 20, 22, 27, 32, 33, 38, 42, 48, 51, 54, 57],
		 'Антон Новиков': [4, 8, 9, 15, 18, 24, 26, 31, 33, 40, 41, 47, 51, 55, 59],
		 'Михаил Петухов': [4, 6, 11, 13, 20, 23, 27, 29, 34, 40, 43, 48, 50, 53, 59],
		 'Наталья Долгушина': [2, 8, 11, 14, 17, 23, 25, 31, 36, 38, 44, 48, 49, 55, 58],
		 'Дмитрий Быков': [4, 5, 12, 14, 19, 24, 28, 29, 35, 38, 43, 47, 49, 54, 60],
		 'Юлия Логинова': [1, 6, 10, 14, 18, 21, 25, 29, 33, 37, 41, 48, 52, 56, 60],
		 'Дмитрий Зайчиков': [1, 7, 11, 15, 19, 22, 25, 30, 35, 40, 44, 45, 52, 54, 59],
		 'Сергей Мазаев': [1, 8, 12, 16, 20, 22, 26, 29, 36, 39, 42, 46, 49, 56, 59],
		 'Влад Мамин': [2, 7, 12, 13, 18, 21, 27, 31, 35, 39, 44, 46, 51, 53, 60],
		 'Дмитрий Новиков': [4, 7, 10, 16, 17, 22, 28, 31, 34, 37, 41, 45, 49, 53, 57],
		 'Андрей Ланцов': [1, 5, 9, 13, 17, 23, 26, 32, 35, 37, 42, 45, 50, 55, 60],
		 'Елена Фадина': [2, 6, 9, 16, 19, 23, 28, 30, 33, 39, 42, 47, 52, 53, 58],
		 'Леон Николаев': [3, 8, 10, 13, 19, 24, 25, 32, 34, 39, 43, 45, 51, 56, 58],
		 'Кирилл Хромов': [3, 6, 12, 15, 17, 21, 26, 30, 34, 38, 44, 47, 50, 56, 57]}
part = {1: ['Андрей Ланцов', 'Юлия Логинова', 'Дмитрий Зайчиков', 'Сергей Мазаев'],
		2: ['Евгения Нетребина', 'Елена Фадина', 'Влад Мамин', 'Наталья Долгушина'],
		3: ['Александр Невзоров', 'Кирилл Хромов', 'Ольга Алексеева', 'Леон Николаев'],
		4: ['Дмитрий Быков', 'Михаил Петухов', 'Дмитрий Новиков', 'Антон Новиков'],
		5: ['Андрей Ланцов', 'Евгения Нетребина', 'Александр Невзоров', 'Дмитрий Быков'],
		6: ['Юлия Логинова', 'Елена Фадина', 'Кирилл Хромов', 'Михаил Петухов'],
		7: ['Дмитрий Зайчиков', 'Влад Мамин', 'Ольга Алексеева', 'Дмитрий Новиков'],
		8: ['Сергей Мазаев', 'Наталья Долгушина', 'Леон Николаев', 'Антон Новиков'],
		9: ['Андрей Ланцов', 'Елена Фадина', 'Ольга Алексеева', 'Антон Новиков'],
		10: ['Юлия Логинова', 'Евгения Нетребина', 'Леон Николаев', 'Дмитрий Новиков'],
		11: ['Дмитрий Зайчиков', 'Наталья Долгушина', 'Александр Невзоров', 'Михаил Петухов'],
		12: ['Сергей Мазаев', 'Влад Мамин', 'Кирилл Хромов', 'Дмитрий Быков'],
		13: ['Андрей Ланцов', 'Влад Мамин', 'Леон Николаев', 'Михаил Петухов'],
		14: ['Юлия Логинова', 'Наталья Долгушина', 'Ольга Алексеева', 'Дмитрий Быков'],
		15: ['Дмитрий Зайчиков', 'Евгения Нетребина', 'Кирилл Хромов', 'Антон Новиков'],
		16: ['Сергей Мазаев', 'Елена Фадина', 'Александр Невзоров', 'Дмитрий Новиков'],
		17: ['Андрей Ланцов', 'Наталья Долгушина', 'Кирилл Хромов', 'Дмитрий Новиков'],
		18: ['Юлия Логинова', 'Влад Мамин', 'Александр Невзоров', 'Антон Новиков'],
		19: ['Дмитрий Зайчиков', 'Елена Фадина', 'Леон Николаев', 'Дмитрий Быков'],
		20: ['Сергей Мазаев', 'Евгения Нетребина', 'Ольга Алексеева', 'Михаил Петухов'],
		21: ['Юлия Логинова', 'Кирилл Хромов', 'Влад Мамин', 'Ольга Алексеева'],
		22: ['Дмитрий Зайчиков', 'Сергей Мазаев', 'Евгения Нетребина', 'Дмитрий Новиков'],
		23: ['Наталья Долгушина', 'Андрей Ланцов', 'Михаил Петухов', 'Елена Фадина'],
		24: ['Леон Николаев', 'Антон Новиков', 'Александр Невзоров', 'Дмитрий Быков'],
		25: ['Юлия Логинова', 'Дмитрий Зайчиков', 'Наталья Долгушина', 'Леон Николаев'],
		26: ['Кирилл Хромов', 'Сергей Мазаев', 'Андрей Ланцов', 'Антон Новиков'],
		27: ['Влад Мамин', 'Евгения Нетребина', 'Михаил Петухов', 'Александр Невзоров'],
		28: ['Ольга Алексеева', 'Дмитрий Новиков', 'Елена Фадина', 'Дмитрий Быков'],
		29: ['Юлия Логинова', 'Сергей Мазаев', 'Михаил Петухов', 'Дмитрий Быков'],
		30: ['Кирилл Хромов', 'Дмитрий Зайчиков', 'Елена Фадина', 'Александр Невзоров'],
		31: ['Влад Мамин', 'Дмитрий Новиков', 'Наталья Долгушина', 'Антон Новиков'],
		32: ['Ольга Алексеева', 'Евгения Нетребина', 'Андрей Ланцов', 'Леон Николаев'],
		33: ['Юлия Логинова', 'Евгения Нетребина', 'Елена Фадина', 'Антон Новиков'],
		34: ['Кирилл Хромов', 'Дмитрий Новиков', 'Михаил Петухов', 'Леон Николаев'],
		35: ['Влад Мамин', 'Дмитрий Зайчиков', 'Андрей Ланцов', 'Дмитрий Быков'],
		36: ['Ольга Алексеева', 'Сергей Мазаев', 'Наталья Долгушина', 'Александр Невзоров'],
		37: ['Юлия Логинова', 'Дмитрий Новиков', 'Андрей Ланцов', 'Александр Невзоров'],
		38: ['Кирилл Хромов', 'Евгения Нетребина', 'Наталья Долгушина', 'Дмитрий Быков'],
		39: ['Влад Мамин', 'Сергей Мазаев', 'Елена Фадина', 'Леон Николаев'],
		40: ['Ольга Алексеева', 'Дмитрий Зайчиков', 'Михаил Петухов', 'Антон Новиков'],
		41: ['Дмитрий Новиков', 'Ольга Алексеева', 'Антон Новиков', 'Юлия Логинова'],
		42: ['Андрей Ланцов', 'Сергей Мазаев', 'Елена Фадина', 'Евгения Нетребина'],
		43: ['Леон Николаев', 'Александр Невзоров', 'Дмитрий Быков', 'Михаил Петухов'],
		44: ['Дмитрий Зайчиков', 'Влад Мамин', 'Кирилл Хромов', 'Наталья Долгушина'],
		45: ['Дмитрий Новиков', 'Андрей Ланцов', 'Леон Николаев', 'Дмитрий Зайчиков'],
		46: ['Ольга Алексеева', 'Сергей Мазаев', 'Александр Невзоров', 'Влад Мамин'],
		47: ['Антон Новиков', 'Елена Фадина', 'Дмитрий Быков', 'Кирилл Хромов'],
		48: ['Юлия Логинова', 'Евгения Нетребина', 'Михаил Петухов', 'Наталья Долгушина'],
		49: ['Дмитрий Новиков', 'Сергей Мазаев', 'Дмитрий Быков', 'Наталья Долгушина'],
		50: ['Ольга Алексеева', 'Андрей Ланцов', 'Михаил Петухов', 'Кирилл Хромов'],
		51: ['Антон Новиков', 'Евгения Нетребина', 'Леон Николаев', 'Влад Мамин'],
		52: ['Юлия Логинова', 'Елена Фадина', 'Александр Невзоров', 'Дмитрий Зайчиков'],
		53: ['Дмитрий Новиков', 'Елена Фадина', 'Михаил Петухов', 'Влад Мамин'],
		54: ['Ольга Алексеева', 'Евгения Нетребина', 'Дмитрий Быков', 'Дмитрий Зайчиков'],
		55: ['Антон Новиков', 'Андрей Ланцов', 'Александр Невзоров', 'Наталья Долгушина'],
		56: ['Юлия Логинова', 'Сергей Мазаев', 'Леон Николаев', 'Кирилл Хромов'],
		57: ['Дмитрий Новиков', 'Евгения Нетребина', 'Александр Невзоров', 'Кирилл Хромов'],
		58: ['Ольга Алексеева', 'Елена Фадина', 'Леон Николаев', 'Наталья Долгушина'],
		59: ['Антон Новиков', 'Сергей Мазаев', 'Михаил Петухов', 'Дмитрий Зайчиков'],
		60: ['Юлия Логинова', 'Андрей Ланцов', 'Дмитрий Быков', 'Влад Мамин']}
posgames = set()
for i in part:
	if set(part[i]).issubset(people):
		posgames.add(i)
for i in posgames:
	print(i, part[i])