import csv
import random
import time
class Question:
    answers = []
    corrects = []

    def __init__(self, num=0):
        self.num = num

    def give_question(self):
        with open('questions1.csv', "rt", newline="") as questions_list:
            reader = csv.reader(questions_list, delimiter=",")
            for row in reader:
                self.answers.append(row)
            question = self.answers[self.num][0]
            q_answer = self.answers[self.num][1:]
            random.shuffle(q_answer)
            print(question, *q_answer, sep ="\n")
    def give_answer(self, char=' '):
        if (char) == self.answers[len(self.answers) - 1][self.num].lstrip()[0]:
            return 1
        else:
            return 0



def main():
    players = [0, 0]
    print("Добро пожаловать в Викторину!")
    time.sleep(3)
    print("----------------------------------")
    print("Суть игры: отвечать на вопросы по-очередно.")
    print("Ответы принимаются только в формате английских букв.")
    print("На каждый вопрос дается 10 секунд.")
    print("В случае неправильного ввода или пропуске вопроса балл не дается.")
    print("----------------------------------")
    time.sleep(5)
    nums = [x for x in "0123456789"]
    random.shuffle(nums)
    for i in range(10):
        question = Question(int(nums[i]))
        print(f"Ход {i%2 + 1} игрока : ")
        question.give_question()
        players[i%2] += question.give_answer(input("Введите ответ: "))
        print()
        time.sleep(1)

    print("\nИГРА ОКОНЧЕНА!")
    print("Победитель игрок: 1" if players[0] > players[1] else "Победитель игрок: 2" if players[0] < players[1] else "НИЧЬЯ!")
    print("----------------------------------")
    print(f"Счет 1 игрока: {players[0]}/5")
    print(f"Счет 2 игрока: {players[1]}/5")
    print("----------------------------------")
if __name__ == '__main__':
    main()
