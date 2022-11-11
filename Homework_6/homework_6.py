import random

points_counter = 0
games_counter = 0

print("Введите ваше имя")
# прога приветствует пользователя и запрашивает его имя
user_name = input()

with open("words.txt", encoding="utf-8") as file:
    # игроку выдаеться по очереди слово с перемешанными буквами из файла words.txt
    for word in file:
        words = list(word.strip("\n"))
        random.shuffle(words)
        jumbled_word = "".join(words)

        # программа выдает правильный/неправильный ответ и прибовляет очки
        print(f"Угадай слово: {jumbled_word}\n")
        user_answer = input()

        if user_answer == word.strip("\n"):
            print("Верно! Вы получаете 10 очков.")
            points_counter += 10
        else:
            print(f"Неверно! Верный ответ – {word}.")

with open("history.txt", "w", encoding="utf-8") as file:
    ''' имя игрока и его очки добовляются в файл history.txt '''
    file.write(f"{user_name} {points_counter} \n")

with open("history.txt", "r+", encoding="utf-8") as file:
    # программа подсчитывает полную статистику
    for user_score in file:
        name, score = user_score.rstrip().split()
        games_counter += 1
    max_result = max(score)

# вывод всей статистики
print(f"Всего игр сыграно: {games_counter}")
print(f"Максимальный рекорд: {max_result}")
