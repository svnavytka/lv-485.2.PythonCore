#Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел. 
# def average(*args):
#     avg = sum(args)/len(args)
#     print("Average sum: ", avg)
#     return avg
#Написати функцію, яка повертає абсолютне значення числа
# integer = int(input('Type number: '))
# print(abs(integer))

#Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації DocStrings.
# def max_number(a,b):
#   ''' This function returns maximum number out of two given.'''
#   if a > b:
#       max = a
#   else: max = b
#   return max

#Написати програму, яка обчислює площу прямокутника, трикутника та кола
# (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)
# def rectangle():
#   l = int(input('Legnth of rectangle: '))
#   w = int(input('Width of rectangle: '))
#   if l >= 1 and w >= 1:
#     print('Rectangle area is: ', l*w)
#   else:
#     print('Legnth and width shouldn\'t be less than 1')
#     rectangle()

# def triangle():
#   h = int(input('Height of triangle: '))
#   b = int(input('Base of triangle: '))
#   if h >= 1 and b >= 1:
#       print('Triangle area is: ', (h*b)/2)
#   else:
#     print('Height and base shouldn\'t be less than 1')
#     triangle()

# def circle():
#   PI = 3.14
#   r = int((input('Radius of circle: ')))
#   if r >= 1:
#     print('Circle area is: ', PI*(r**2))
#   else:
#     print('Radius shouldn\'t be less than 1')
#     circle()
    
# area = int(input('What area you want to find? If rectangle - print number 1, triangle - 2, circle - 3: '))
# while area != 1 and area != 2 and area !=3:
#     print('Choose between numbers 1, 2 or 3')
#     area = int(input('What area you want to find? If rectangle - print number 1, triangle - 2, circle - 3: '))
# if area == 1:
#     rectangle()
# if area ==2:
#     triangle()
# elif area == 3:
#     circle()