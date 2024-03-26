# -*- coding: cp1251 -*-

import random
from unicodedata import normalize

while True:
    checker = False
    primaryChoice = input("Выбор задания для проверки : \n1)\n2)\n3)\n4)\n5) - Выход\nВыбор : ")
    if [num for num in primaryChoice if num not in ".,/*-+1234567890"]: checker = True
    if checker == True:
        print("Так нельзя")
        break
    primaryChoice = int(primaryChoice)

    if primaryChoice == 1:
        counter = 0
        numOfWords = input("Введите количество сообщений, которые вы отправите ")
        numOfWords = int(numOfWords)
        famousLastWords = " "
        while counter < numOfWords:
            checker = False
            newWords = input("Введите слово : ")
            if [num for num in newWords if num in ".,/*-+1234567890"]: checker = True
            if checker == True:
                print("Так нельзя")
                break
            newWords = newWords.replace(" ", "")
            counter += 1
            
            famousLastWords += newWords
            famousLastWords += " "
            print("Пока получается :" + famousLastWords)

    if primaryChoice == 2 :
        famousLastWords = " "
        print("Чтобы остановить программу введите слово Стоп")
        while True:        
            checker = False
            newWords = input("Введите слово : ")
            if [num for num in newWords if num in ".,/*-+1234567890"]: checker = True
            if checker == True:
                print("Так нельзя")
                break
            newWords = newWords.replace(" ", "")
            
            famousLastWords += newWords
            famousLastWords += " "
            print("Пока получается :" + famousLastWords)
        
            if newWords == "Стоп":
                break
            
    if primaryChoice == 3:
        print("Впишите слово стоп, чтобы остановить программу")
        while True:
            uniqueChecker = False
            wordToCheck = input("Введите слово на проверку : ")
            wordToCheck = wordToCheck.lower()
            if [letter for letter in wordToCheck if letter in "ф"]: uniqueChecker = True
            if uniqueChecker == True:
                print("Ого! Это редкое слово")
            else:
                print("Эх, это не очень редкое слово...")
            if wordToCheck == "стоп":
                break

    if primaryChoice == 4:
        
        countWrong = 3
        
        while True:
            
            
            firstNum = random.randint(-50, 50)
            secondNum = random.randint(-50, 50)
            choicer = random.randint(1, 2)
            print("Готовы начать 1 - да 2 - нет")
            ender = input()
            ender = int(ender)
            
            if ender == 1:
        
                if choicer == 1: 
                    rightAns = firstNum + secondNum
                    print(str(firstNum) + " + " + str(secondNum))
                    print("Какое число выйдет ?")
                    personChoice = input()
                    personChoice = int(personChoice)
                    if personChoice == rightAns:
                        print ("Правильно")
                        print("Хотите попробовать еще ? 1 - да 2 - нет" )
                        ender = input()
                        ender = int(ender)
                    else:
                        print("Неправильно, верный ответ " + str(rightAns))
                        print("Осталось попыток " + str(countWrong))
                        print("Хотите попробовать еще ? 1 - да 2 - нет" )
                        countWrong = countWrong - 1
                        ender = input()
                        ender = int(ender)
                        
                if choicer == 2:
                    rightAns = firstNum - secondNum
                    print(str(firstNum) + "-" + str(secondNum))
                    print("Какое число выйдет ?")
                    personChoice = input()
                    personChoice = int(personChoice)
                    if personChoice == rightAns:
                        print ("Правильно")
                        print("Хотите попробовать еще ? 1 - да 2 - нет" )
                        ender = input()
                        ender = int(ender)
                    else:
                        print("Неправильно, верный ответ "+ str(rightAns))
                        print("Осталось попыток " + str(countWrong))
                        print("Хотите попробовать еще ? 1 - да 2 - нет" )
                        countWrong = countWrong - 1
                        ender = input()
                        ender = int(ender)
                        
            elif ender == 2 or countWrong == 0:
                break 
        
 
    if primaryChoice == 5:
        break