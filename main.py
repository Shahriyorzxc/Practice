# num = int(input("Son:" ))
# if num % 2 == 0:
#     print("Juft son ")
# else:
#     print("Juft emas ")
#
#
# while True:
#     number = int(input("Son: "))
#     if number < 0 and number <= 4 or number > 60:
#         print("Bepul")
#     elif number > 4 and number <= 18:
#         print("10000")
#     elif number > 18 and number <= 60:
#         print("20000")
#     else:
#         print("Manfiy son mumkin emas! ")
#
#
#     number = int(input("Son: "))
#     print(f"{number} soni uchun keyingi {number + 1}")

# lst = ["Ali", "Vali", "Vali", "Vali", "Vali", "Vali", "Vali", "Almardon", "Sardor", "Jahongir", "Aziz"]
# lst.sort()
# print(lst)
# lst.reverse()
# print(lst)
#
# # listni ichia qidiruv
# if lst[3] == "Ali":
#     print("Salom")
#
# else:
#     print("Yoq")
# # listni yangilash
# lst[0] = "Doniyor"
# print(lst)
#
#
# # List Metodlari
# # qoshish metodlari
# lst.append("Ali") # oxiridan qo'shadi
# print(lst)
#
# lst.insert(3, "Sarvar")
# print(lst)
# #
#
# #
# lst1 = ["Ali", "Vali", "Sardor", "Jahongir", "Aziz"]
# lst2 = ["Shahriyor", "Ozodbek"]
# lst2.extend(lst1)
# print(lst1)
# print(lst2)
#
# lst1 = ["Ali", "Vali", "Sardor", "Jahongir",23, "Aziz"]
#
# # #Ochirish metodlari
# lst.clear()
# print(lst)
# lst1.remove("Aziz")
# print(lst1)
#
# lst_pop = lst1.pop(0) #ctr + x
# print(lst_pop)
# print(lst1)
#
#
# lst2 = [5, 6, 3, 2, 9, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1]
# lst2.sort()
#
# copy_lst2 = lst2.copy()
# print(copy_lst2)
# print(lst2)
# lst3 = [True, True, True, True, True, True, False]
# lst_count = lst2.count(1)
# name_count = lst.count("Vali")
# booling_lst = lst3.count(True)
# print(booling_lst)
#
# lst4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst4.reverse()
# print(lst4)

# lst = [1,2,3,4,5,[True, False, 'a', 'b']]
# x = lst.index(1)
# print(x)
#
# y = lst.count(True)
# print(y)

#True = 1
#False = 0

#for ssikl
# lst = [1,2,3,4,5,6,7,8,9,10]
# item = int(input("Son: "))
# if item in lst:
#     print("Bor")
#
# else:
#     print("Yoq")
#
# for x in lst:
#     if x == 5:
#         print("Bor")
# while True:
#     print("Agar dollardan -> so'mga otish uchun 1 ni bosing!\nAgar so'mdan -> dollarga otish uchun 2 ni bosing!")
#     tanlov = input("Son: ")
#     if tanlov == "1":
#         print("So'm kursini aniqlash!")
#         dollar = int(input("Dollar: "))
#         print(f"So'm: {dollar * 12450}")
#
#     elif tanlov == "2":
#         print("Dollar kursini aniqlash!")
#         som = int(input("So'm: "))
#         print(f"Dollar: {som // 12450}")
#
# print(2 != 2)
#
#
# lst = [1,2,3,4,5,6,7,8,9,10]
# result = 1
# for x in lst:
#     result += x  # result = result * x
#
# print(result)
#
# #range
# result = 0
# for x in range(1, 11):
#     result += x
#
# print(result)
#
# #factorial 5! = 1*2*3*4*5
# while True:
#     n = int(input("Son: "))
#     result = 1
#     for x in range(1, n + 1):
#         result *= x
#     print(result)


# names = ["Ali", "Vali", "Bunyod", "Komil", "Shaxriyor"]
# # lenth = len(names)
# # print(lenth)
# for name in names:
#     print(f'Salom {name}')
# print(f"Kod {len(names)} marta ishladi!")
#
#
#
# for num in range(1, 11):
#     if num % 2 != 0:
#         print(num ** 3)
#
# # ism = []
# # young = int(input("Suxbat soni: "))
# # for num in range(1, young + 1):
# #     name = input(f"{num} - suxbat qilgan odamingiz kim edi: ")
# #     ism.append(name)
# #
# # print(ism)
#
#
# #
# # for num in range(1, 11):
# #     if num % 2 != 0:
# #         print(num ** 3)
#
# # range(start, stop, step) range integer qabul qiladi.
# # for x in range(11, 100, 2):
# #     print(x ** 3)
# #
# # print('Hello world')
#
#
# # while ssikl o'ziga shart qabul qiladi.
# # Iteratsiya bo'ladigan ma'lumotlarga index orqali murojat qiladi
# nums = [1, 2, 3, 4, 5, 6, 7]
#
# index = 0
# while index < len(nums):
#     num = nums[index]
#     index = index + 1
#     print(num)
#
# print("Hello world!")
#
# for num in nums:
#     print(num)

# print(4 ** 1//2)
#
# a = 3
# b = 4
# print(((a  2) + (b  2)) ** (1/2))


# i = 0
# while i < 100:
#     print(i)
#     i += 1
#
# for num in range(1, 100):
#     print(num)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1

# for x in range(1, 10):
#     print(nums[x])
#

# for x in range(1, 10):
#     print("!")
#
# for x in nums:
#     print(x)


# lst = [1,2,34,56,78]
# l = 0
# for x in lst:
#     l += x
# print(l)
#---------------------------------
# nums = [1,2,3,4,5,6]
# i = 0
# while i < len(nums):
#     x = nums[i]
#     print(nums[i])
#     i += 1
#---------------Task-----------------------------------------
# names = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
# print(names[0])
# i = 0
# while i < len(names):
#     name = names[i]
#     print(f"Salom {name}!")
#     i += 1
#
# print(f"Kod {len(names)} ta takrorlandi!")

# i = 0
# nums = list(range(10, 101))
# print(nums)
# while i < len(nums):
#     num = nums[i]
#     if num % 2 != 0:
#         print(num  3)
#     i += 1

#
# for x in nums:
#     if x % 2 != 0:
#         print(x  3)


# names = []
#
# count_name = int(input("Bugun nechi kishi b-n suxbat qildingiz: "))
#
# i = 1
# while i < count_name:
#     name = input(f"{i} - suxbat qilgan odamingiz kim edi: ")
#     names.append(name)
#     i += 1
#
# print(names)

# --------Lug'atlar -> dict()--------------------------------------------------------------------------
# personal_details = {
#     "Sardor": {
#         "age": 17,
#         "phone_numbers": {
#             'home_phone': 95195951,
#             "mobile_phone": 948498
#         },
#         "location": "Olmaliq"
#     },
#     "Komil": {
#         "age": 17,
#         "phone_number": 901234567,
#         "location": "Olmaliq"
#     }
# }
# print(personal_details)

# person = {
#     'name': 'Sardor',
#     'age': 17
# }
# print(person["name"]) #qiymat olish
# person["name"] = "Doniyor" #dict ichidagi elementni key orqali qiymatini o'zgartirish
# person["location"] = "Olmaliq"#dict ichiga ma'lumot qo'shish
# print(person)
#
# for item in person: # Key va valueni olvolish
#     print(f"Key: {item} - Value: {person[item]}")
#


# --------------------------------------------------------------
# personal_details = {
#     "Sardor": {
#         "age": 17,
#         "phone_numbers": {
#             'home_phone': 95195951,
#             "mobile_phone": 948498
#         },
#         "location": "Olmaliq"
#     },
#     "Komil": {
#         "age": 17,
#         "phone_number": 901234567,
#         "location": "Olmaliq"
#     }
# }

# print(personal_details["Sardor"]["phone_numbers"]["home_phone"])
# print(personal_details.get("Komil").get("phone_number"))


# -------Metodlar-------------------------------------------------------

# person = {
#     'name': 'Sardor',
#     'age': 17
# }

# # person.clear() #lugatni tozalaydi!
# # young = person.pop("age") #ctrl + x
# # dict_copy = person.copy() #copiya
# key, value = person.popitem() #lug'atni oxirgi elementini ochiradi, key value saqlidi
# print(key, value)
# loc = {
#     "location": "Olmaliq",
#     'address': "Amir Temur 9"
# }
# person.update(loc)


# person = {
#     'name': 'Sardor',
#     'age': 17
# }
# for key, value in person.items(): #key value olib keladi
#     print(key, value)
#
# for key in person.keys(): #faqat keyni olib keladi
#     print(key)

# for value in person.values():
#     print(value)

# menu = {
#     "osh": "25000 so'm",
#     "kabob": "20000 so'm",
#     "norin": "25000 so'm",
#     "sho'rva": "25000 so'm",
#     "manti": "5000 so'm",
#     "lag'mon": "25000 so'm",
#     "pepsi": "13000 so'm",
#     "choy": "5000 so'm",
#     "non": "5000 so'm"
# }
#
# for x in range(1, 4):
#     taom = input(f"{x} taom: ")
#     if taom in menu:
#         print(menu[taom])
#
#     else:
#         print("Bunday taom yoq!")
#
#
# def birthday():
#     name = input("Ism: ")
#     age = int(input("Yosh: "))
#     return f"{name} tugilgan yili - {2024 - age}"
#
#
# print(birthday())
#

# def RangeNum(num1, num2):
#     lst = []
#     for x in range(num1 + 1, num2):
#         lst.append(x)
#     return lst
#
#
# print(RangeNum(2,4))
# print(RangeNum(5,9))
#

# def isFourLetters(lst):
#     lst1 = []
#     for x in lst:
#         if len(x) == 4:
#             lst1.append(x)
#     return lst1
#
#
# print(isFourLetters(['Tomato', 'Potato', 'Pair']))
# print(isFourLetters(['Kangaroo', 'Bear', 'Foxs']))
#

# def firstLast(lst):
#     lst1 = []
#     lst1.append(lst[0])
#     lst1.append(lst[-1])
#     return lst1
#
#
# print(firstLast([1, 2, 3, 54, 67, 89]))

# O'zgaruvchilar
# name = 'Sarvar'


# istisno tenglikning chap tarafadigi ozgaruvchilar miqdori
# tenglikning ong tomonidagi malumotlar miqdoriga teng bo'lishi kerak
# x, y, z = 1, 'son', True
# # x = 1
# # y = 'son'
# # z =  True
# print(x, y, z)
# print(x) #1
# print(y) #3
# print(z)#2

#
# x = y = z = 'Olma'
# x = 'Olma'
# y = x
# z = y
# print(x)
# print(y)
# print(z)

# 3 turdagi sonlar mavjud int, float, comoplex
# Complex sonlarga misol 4 - 3*i => bu yerda i = -1
# Natija = 4 - 3 * (-1) = 4 + 3 = 7

# Malumot turlari 2 xil bo'ladi.
# print(type(1))
# 1 - Ozgaruvchan malumot turlari => list, dict, set.  lst = [1,3,5,7]  lst.append(4)
# 2 - Ozgarmas malumot turlari => number (int, float, complex), str, booling, tuple

# string malumot turi
# name = 'Shaxriyor'

# string ichiga index bo'ycha murojat qilsak bo'ladi
# print(f"{name} ismida {name[4]} xarfi bor!")

# stringda [start:stop:step]
# print(name[0:6:2])

# stringda ssikllar
# for x in name:
#     if x == 'a':
#         print(f"{name} ismida {x} xarfi bor!")

    # -----ekvivalent-----------------------------------------------
# i = 0
# while i < len(name):
#     x = name[i]
#     if x == 'a':
#         print(f"{name} ismida {x} xarfi bor!")
#     i += 1


# task1
# def jazzify(lst):
#     lstk = []
#     for x in lst:
#         lstk.append(f"{x}7 ")
#     return lstk
#
#
# print(jazzify(["G", "F", "C"]))  # -> ["G7", "F7", "C7"]

#String metod
# name = 'sarDoR'
# x = name.count('r')
# print(x)
#
# y = name.index('D')
# print(y)
#
# z = name.lower()
# print(z)
#
# z1 = name.upper()
# print(z1)
#
# z2 = name.capitalize()
# print(z2)
#
# n = 'Kamoliddin'
# z3 = "Mening ismim {}".format(n)
# z4 = f"Mening ismim {n}"
# print(z3)
# print(z4)
#
# content = 'Lorem Ipsum - это текст-"рыба", часто используемый'
# z5 = content.split('-')
# print(z5)
#
# lorem = 'Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение букв и пробелов в абзацах, которое не получается при простой дубликации'
#
# b = lorem.split('.')
# print(len(b))
#
# name1 = 'sarDoR'
# c = "#".join(name1)
# print(c)

# list typedan -> str type ga otishda
# lst1 = ['a', 'b', 'c']
# d = '*'.join(lst1)
# print(d)
# print(type(d))
#
# name2 = '1212'
# x1 = name2.isalnum()
# print(x1)
#
# password = input("Password: ")
# if password.isalnum():
#     print("Correct!")
# else:
#     print('Error!')

#-----------------------------ffffffff
# name3 = 'asdwqd'
# print(name3.isalpha())  # True
# name4 = '21'
# print(name3.isdigit())  # True
# name5 = 'dqwwq'
# print(name5.isupper())  # FALSE
# print(name5.islower())  # True
#-------------------------------
# pasword = input('Password: ')
# f = pasword.strip()
# if len(f) < 8:
#     print(len(f))
#     print("Password 8 ta simboldan iborat bo'lishi kerak!")
#
# else:
#     print("Correct!")
#
# content1 = 'Mashina'
# ch = content1.replace('sh', 'w')
# print(content1)
# print(ch)
#
# print(2 * "5")





































def calculate_age(year_of_birth):
    current_year = 2024
    age = current_year - year_of_birth
    return age

def main():
    year_of_birth = int(input("Введите год рождения: "))
    age = calculate_age(year_of_birth)
    print(f"Ваш возраст: {age} лет.")

if __name__ == "main":
    main()

def input_numbers():
    num_list = []
    n = int(input("Введите количество чисел в списке: "))
    for i in range(n):
        num = int(input("Введите число: "))
        num_list.append(num)
    return num_list

def sort_list(lst):
    sorted_lst = sorted(lst)
    return sorted_lst

def sum_list(lst):
    total = sum(lst)
    return total

# Ввод чисел пользователем
lst = input_numbers()

# Сортировка списка
sorted_lst = sort_list(lst)

# Подсчет суммы всех чисел в списке
total_sum = sum_list(lst)

# Вывод результатов
print("Отсортированный список:", sorted_lst)
print("Сумма всех чисел в списке:", total_sum)




def count_words(word_list):
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def print_word_count(word_count):
    print("Слова и их количество в списке:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

def main():
    # Создаем пустой список слов
    words = []

    # Запрашиваем у пользователя ввод слов, пока он не введет пустую строку
    while True:
        word = input("Введите слово (или нажмите Enter для завершения): ")
        if word == "":
            break
        words.append(word)

    # Подсчитываем количество вхождений каждого слова
    word_count = count_words(words)

    # Выводим результаты
    print_word_count(word_count)

if __name__ == "main":
    main()



class ToDoList:
    def init(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def remove_task(self, task_index):
        del self.tasks[task_index]

    def mark_task_as_completed(self, task_index):
        self.tasks[task_index] = True

    def display_tasks(self):
        print("Ваш список задач:")
        for index, task in enumerate(self.tasks, start=1):
            status = "выполнено" if task["completed"] else "не выполнено"
            print(f"{index}. {task['task']} - {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Отметить задачу как выполненную")
        print("4. Показать список задач")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            task = input("Введите новую задачу: ")
            todo_list.add_task(task)
        elif choice == "2":
            if todo_list.tasks:
                task_index = int(input("Введите номер задачи для удаления: ")) - 1
                todo_list.remove_task(task_index)
            else:
                print("Список задач пуст.")
        elif choice == "3":
            if todo_list.tasks:
                task_index = int(input("Введите номер задачи для отметки как выполненной: ")) - 1
                todo_list.mark_task_as_completed(task_index)
            else:
                print("Список задач пуст.")
        elif choice == "4":
            if todo_list.tasks:
                todo_list.display_tasks()
            else:
                print("Список задач пуст.")
        elif choice == "5":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "main":
    main()





class ExpenseTracker:
    def init(self):
        self.expenses = []

    def add_expense(self, date, amount, description):
        self.expenses.append({"date": date, "amount": amount, "description": description})

    def remove_expense(self, expense_index):
        del self.expenses[expense_index]

    def total_expenses(self):
        total = sum(expense["amount"] for expense in self.expenses)
        return total

    def expenses_in_period(self, start_date, end_date):
        expenses_in_period = [expense["amount"] for expense in self.expenses
                              if start_date <= expense["date"] <= end_date]
        total_in_period = sum(expenses_in_period)
        return total_in_period

    def display_expenses(self):
        print("Все расходы:")
        for index, expense in enumerate(self.expenses, start=1):
            print(f"{index}. {expense['date']} - ${expense['amount']}: {expense['description']}")

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\n1. Добавить расход")
        print("2. Удалить расход")
        print("3. Показать общую сумму расходов")
        print("4. Показать сумму расходов за период")
        print("5. Показать все расходы")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            date = input("Введите дату расхода (гггг-мм-дд): ")
            amount = float(input("Введите сумму расхода: $"))
            description = input("Введите описание расхода: ")
            expense_tracker.add_expense(date, amount, description)
        elif choice == "2":
            if expense_tracker.expenses:
                expense_index = int(input("Введите номер расхода для удаления: ")) - 1
                expense_tracker.remove_expense(expense_index)
            else:
                print("Список расходов пуст.")
        elif choice == "3":
            total = expense_tracker.total_expenses()
            print(f"Общая сумма расходов: ${total}")
        elif choice == "4":
            start_date = input("Введите начальную дату периода (гггг-мм-дд): ")
            end_date = input("Введите конечную дату периода (гггг-мм-дд): ")
            total_period = expense_tracker.expenses_in_period(start_date, end_date)
            print(f"Сумма расходов за период с {start_date} по {end_date}: ${total_period}")
        elif choice == "5":
            if expense_tracker.expenses:
                expense_tracker.display_expenses()
            else:
                print("Список расходов пуст.")
        elif choice == "6":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "main":
    main()












class GameLibrary:
    def init(self):
        self.games = []

    def add_game(self, title, genre, platform):
        self.games.append({"title": title, "genre": genre, "platform": platform})

    def remove_game(self, title):
        for game in self.games:
            if game["title"] == title:
                self.games.remove(game)
                return
        print(f"Игра с названием '{title}' не найдена в библиотеке.")

    def display_all_games(self):
        print("Список игр в библиотеке:")
        for index, game in enumerate(self.games, start=1):
            print(f"{index}. {game['title']} - Жанр: {game['genre']}, Платформа: {game['platform']}")

def main():
    game_library = GameLibrary()

    while True:
        print("\n1. Добавить игру")
        print("2. Удалить игру")
        print("3. Показать все игры")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название игры: ")
            genre = input("Введите жанр игры: ")
            platform = input("Введите платформу игры: ")
            game_library.add_game(title, genre, platform)
            print(f"Игра '{title}' успешно добавлена в библиотеку.")
        elif choice == "2":
            title = input("Введите название игры для удаления: ")
            game_library.remove_game(title)
        elif choice == "3":
            if game_library.games:
                game_library.display_all_games()
            else:
                print("Библиотека пуста.")
        elif choice == "4":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "main":
    main()




class DotaPlayers:
    def init(self):
        self.players = []

    def add_player(self, nickname, mmr):
        self.players.append({"nickname": nickname, "mmr": mmr})

    def remove_player(self, nickname):
        for player in self.players:
            if player["nickname"] == nickname:
                self.players.remove(player)
                return
        print(f"Игрок с никнеймом '{nickname}' не найден в базе данных.")

    def display_all_players(self):
        print("Список игроков в базе данных Dota 2:")
        for index, player in enumerate(self.players, start=1):
            print(f"{index}. {player['nickname']} - MMR: {player['mmr']}")

def main():
    dota_players = DotaPlayers()

    while True:
        print("\n1. Добавить игрока")
        print("2. Удалить игрока")
        print("3. Показать всех игроков")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            nickname = input("Введите никнейм игрока: ")
            mmr = int(input("Введите MMR игрока: "))
            dota_players.add_player(nickname, mmr)
            print(f"Игрок '{nickname}' успешно добавлен в базу данных Dota 2.")
        elif choice == "2":
            nickname = input("Введите никнейм игрока для удаления: ")
            dota_players.remove_player(nickname)
        elif choice == "3":
            if dota_players.players:
                dota_players.display_all_players()
            else:
                print("База данных пуста.")
        elif choice == "4":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "main":
    main()






class ExpenseTracker:
    def init(self):
        self.expenses = []

    def add_expense(self, date, amount, category):
        self.expenses.append({"date": date, "amount": amount, "category": category})

    def remove_expense(self, expense_index):
        del self.expenses[expense_index]

    def total_expenses(self):
        total = sum(expense["amount"] for expense in self.expenses)
        return total

    def expenses_in_period(self, start_date, end_date):
        expenses_in_period = [expense["amount"] for expense in self.expenses
                              if start_date <= expense["date"] <= end_date]
        total_in_period = sum(expenses_in_period)
        return total_in_period

    def display_expenses(self):
        print("Все расходы:")
        for index, expense in enumerate(self.expenses, start=1):
            print(f"{index}. {expense['date']} - ${expense['amount']} ({expense['category']})")

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\n1. Добавить трату")
        print("2. Удалить трату")
        print("3. Показать общую сумму расходов")
        print("4. Показать сумму расходов за период")
        print("5. Показать все расходы")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            date = input("Введите дату траты (гггг-мм-дд): ")
            amount = float(input("Введите сумму траты: $"))
            category = input("Введите категорию траты: ")
            expense_tracker.add_expense(date, amount, category)
            print("Трата успешно добавлена.")
        elif choice == "2":
            if expense_tracker.expenses:
                expense_index = int(input("Введите номер траты для удаления: ")) - 1
                expense_tracker.remove_expense(expense_index)
                print("Трата успешно удалена.")
            else:
                print("Список трат пуст.")
        elif choice == "3":
            total = expense_tracker.total_expenses()
            print(f"Общая сумма расходов: ${total}")
        elif choice == "4":
            start_date = input("Введите начальную дату периода (гггг-мм-дд): ")
            end_date = input("Введите конечную дату периода (гггг-мм-дд): ")
            total_period = expense_tracker.expenses_in_period(start_date, end_date)
            print(f"Сумма расходов за период с {start_date} по {end_date}: ${total_period}")
        elif choice == "5":
            if expense_tracker.expenses:
                expense_tracker.display_expenses()
            else:
                print("Список трат пуст.")
        elif choice == "6":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "main":
    main()







class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account_number, initial_balance):
        if account_number in self.accounts:
            print("Счет с таким номером уже существует.")
        else:
            self.accounts[account_number] = initial_balance
            print("Счет успешно открыт.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print("Деньги успешно внесены на счет.")
        else:
            print("Счет с таким номером не найден.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print("Деньги успешно сняты со счета.")
            else:
                print("На счете недостаточно средств.")
        else:
            print("Счет с таким номером не найден.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            balance = self.accounts[account_number]
            print(f"Баланс счета {account_number}: ${balance}")
        else:
            print("Счет с таким номером не найден.")




def main():
    bank = Bank()

    while True:
        print("\n1. Открыть счет")
        print("2. Внести деньги на счет")
        print("3. Снять деньги со счета")
        print("4. Проверить баланс счета")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            account_number = input("Введите номер счета: ")
            initial_balance = float(input("Введите начальный баланс: $"))
            bank.open_account(account_number, initial_balance)
        elif choice == "2":
            account_number = input("Введите номер счета: ")
            amount = float(input("Введите сумму для внесения: $"))
            bank.deposit(account_number, amount)
        elif choice == "3":
            account_number = input("Введите номер счета: ")
            amount = float(input("Введите сумму для снятия: $"))
            bank.withdraw(account_number, amount)
        elif choice == "4":
            account_number = input("Введите номер счета: ")
            bank.check_balance(account_number)
        elif choice == "5":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()









class MovieDatabase:
    def init(self):
        self.movies = []

    def add_movie(self, title, genre, year):
        self.movies.append({"title": title, "genre": genre, "year": year})

    def remove_movie(self, title):
        for movie in self.movies:
            if movie["title"] == title:
                self.movies.remove(movie)
                print(f"Фильм '{title}' успешно удален из базы данных.")
                return
        print(f"Фильм с названием '{title}' не найден в базе данных.")

    def display_all_movies(self):
        print("Список фильмов в базе данных:")
        for index, movie in enumerate(self.movies, start=1):
            print(f"{index}. {movie['title']} - Жанр: {movie['genre']}, Год выпуска: {movie['year']}")



def main():
    movie_database = MovieDatabase()

    while True:
        print("\n1. Добавить фильм")
        print("2. Удалить фильм")
        print("3. Показать все фильмы")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название фильма: ")
            genre = input("Введите жанр фильма: ")
            year = input("Введите год выпуска фильма: ")
            movie_database.add_movie(title, genre, year)
            print(f"Фильм '{title}' успешно добавлен в базу данных.")
        elif choice == "2":
            title = input("Введите название фильма для удаления: ")
            movie_database.remove_movie(title)
        elif choice == "3":
            if movie_database.movies:
                movie_database.display_all_movies()
            else:
                print("База данных пуста.")
        elif choice == "4":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "main":
    main()







class AnimeDatabase:
    def init(self):
        self.anime_list = []

    def add_anime(self, title, genre, episodes):
        self.anime_list.append({"title": title, "genre": genre, "episodes": episodes})

    def remove_anime(self, title):
        for anime in self.anime_list:
            if anime["title"] == title:
                self.anime_list.remove(anime)
                return
        print(f"Аниме с названием '{title}' не найдено в базе данных.")

    def display_all_anime(self):
        print("Список аниме в базе данных:")
        for index, anime in enumerate(self.anime_list, start=1):
            print(f"{index}. {anime['title']} - Жанр: {anime['genre']}, Эпизодов: {anime['episodes']}")

def main():
    anime_database = AnimeDatabase()

    while True:
        print("\n1. Добавить аниме")
        print("2. Удалить аниме")
        print("3. Показать все аниме")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название аниме: ")
            genre = input("Введите жанр аниме: ")
            episodes = input("Введите количество эпизодов: ")
            anime_database.add_anime(title, genre, episodes)
            print(f"Аниме '{title}' успешно добавлено в базу данных.")
        elif choice == "2":
            title = input("Введите название аниме для удаления: ")
            anime_database.remove_anime(title)
        elif choice == "3":
            if anime_database.anime_list:
                anime_database.display_all_anime()
            else:
                print("База данных пуста.")
        elif choice == "4":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "main":
    main()



