# -*- coding: cp1251 -*-

import random
from unicodedata import normalize

while True:
    checker = False
    primaryChoice = input("����� ������� ��� �������� : \n1)\n2)\n3)\n4)\n5) - �����\n����� : ")
    if [num for num in primaryChoice if num not in ".,/*-+1234567890"]: checker = True
    if checker == True:
        print("��� ������")
        break
    primaryChoice = int(primaryChoice)

    if primaryChoice == 1:
        counter = 0
        numOfWords = input("������� ���������� ���������, ������� �� ��������� ")
        numOfWords = int(numOfWords)
        famousLastWords = " "
        while counter < numOfWords:
            checker = False
            newWords = input("������� ����� : ")
            if [num for num in newWords if num in ".,/*-+1234567890"]: checker = True
            if checker == True:
                print("��� ������")
                break
            newWords = newWords.replace(" ", "")
            counter += 1
            
            famousLastWords += newWords
            famousLastWords += " "
            print("���� ���������� :" + famousLastWords)

    if primaryChoice == 2 :
        famousLastWords = " "
        print("����� ���������� ��������� ������� ����� ����")
        while True:        
            checker = False
            newWords = input("������� ����� : ")
            if [num for num in newWords if num in ".,/*-+1234567890"]: checker = True
            if checker == True:
                print("��� ������")
                break
            newWords = newWords.replace(" ", "")
            
            famousLastWords += newWords
            famousLastWords += " "
            print("���� ���������� :" + famousLastWords)
        
            if newWords == "����":
                break
            
    if primaryChoice == 3:
        print("������� ����� ����, ����� ���������� ���������")
        while True:
            uniqueChecker = False
            wordToCheck = input("������� ����� �� �������� : ")
            wordToCheck = wordToCheck.lower()
            if [letter for letter in wordToCheck if letter in "�"]: uniqueChecker = True
            if uniqueChecker == True:
                print("���! ��� ������ �����")
            else:
                print("��, ��� �� ����� ������ �����...")
            if wordToCheck == "����":
                break

    if primaryChoice == 4:
        
        countWrong = 3
        
        while True:
            
            
            firstNum = random.randint(-50, 50)
            secondNum = random.randint(-50, 50)
            choicer = random.randint(1, 2)
            print("������ ������ 1 - �� 2 - ���")
            ender = input()
            ender = int(ender)
            
            if ender == 1:
        
                if choicer == 1: 
                    rightAns = firstNum + secondNum
                    print(str(firstNum) + " + " + str(secondNum))
                    print("����� ����� ������ ?")
                    personChoice = input()
                    personChoice = int(personChoice)
                    if personChoice == rightAns:
                        print ("���������")
                        print("������ ����������� ��� ? 1 - �� 2 - ���" )
                        ender = input()
                        ender = int(ender)
                    else:
                        print("�����������, ������ ����� " + str(rightAns))
                        print("�������� ������� " + str(countWrong))
                        print("������ ����������� ��� ? 1 - �� 2 - ���" )
                        countWrong = countWrong - 1
                        ender = input()
                        ender = int(ender)
                        
                if choicer == 2:
                    rightAns = firstNum - secondNum
                    print(str(firstNum) + "-" + str(secondNum))
                    print("����� ����� ������ ?")
                    personChoice = input()
                    personChoice = int(personChoice)
                    if personChoice == rightAns:
                        print ("���������")
                        print("������ ����������� ��� ? 1 - �� 2 - ���" )
                        ender = input()
                        ender = int(ender)
                    else:
                        print("�����������, ������ ����� "+ str(rightAns))
                        print("�������� ������� " + str(countWrong))
                        print("������ ����������� ��� ? 1 - �� 2 - ���" )
                        countWrong = countWrong - 1
                        ender = input()
                        ender = int(ender)
                        
            elif ender == 2 or countWrong == 0:
                break 
        
 
    if primaryChoice == 5:
        break