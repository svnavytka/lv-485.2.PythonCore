# CW5
#
# Task1 "Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число."
#
# nums = []
# k=int(input("Please enter the count of the elements of sequence: "))
# for i in range(k):
#      n = int(input("Please enter the element: "))
#      nums.append(n)
# print(nums)
# max = nums[0]
# min = nums[0]
# for i in range(k):
#     if nums[i] > max:
#         max = nums[i]
#     if nums[i] < min:
#         min = nums[i]
# print("Maximum number = %d. Minimum number = %d." %(max, min))
#
# Task2 "В інтервалі від 1 до 10 визначити числа 
•  парні, які діляться на 2,
•  непарні, які діляться на 3, 
•  числа, які не діляться на 2 та 3."
#
# x1=[]
# x2=[]
# x3=[]
# for x in range(1, 11):
#     if x % 2 == 0:
#         #print(x, 'is even multiple of 2')
#         x1.append(x)
#     elif x % 3 == 0:
#         #print(x, 'is an odd multiple of 3')
#         x2.append(x)    
#     else:
#         #print(x, 'not divisible by 2 and 3')
#         x3.append(x)
# print(x1)        
# print(x2)
# print(x3)
#
# Task3 "Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)"
#
# number=int(input("Enter number more then 0  "))
# factorial=1
# for i in range(1,number+1):
#     factorial*=i  
# print("Factorial",number,"equal",factorial)
#
# Task4 "Напишіть скрипт, який перевіряє логін, який вводить користувач. 
# Якщо логін вірний (First), то привітайте користувача. 
# Якщо ні, то виведіть повідомлення про помилку. 
# (використайте цикл while)login=input("Enter your login: ")
# while login != str('First'):
#     login=input("Entered login is incorrect! \nEnter your login again: ")
# else:
#     print("Welcome, ", login)
# 
# Task5.  Перший випадок. 
# Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число. При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).
# mylist=[]
# n = int(input("Please enter the element: "))
# while n > 0:
#     mylist.append(n)
#     n = int(input("Please enter the element: "))
# else:
#     print(mylist)
# Task 6.  Другий випадок. 
# На початку на вхід подається кількість елементів послідовності, а потім самі елементи. При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).'''
# nums = []
# k=int(input("Please enter the count of the elements of sequence: "))
# for i in range(k):
#      n = int(input("Please enter the element: "))
#      nums.append(n)
#      if n>0:
#        continue
#      else:
#        nums.pop()
#        break
# print("You enter not valid value")