#Task 1
def my_func (*args):
    """Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел. """
    print(sum(args)/len(args))

my_func(10, 10, 20, 10)   
#Task 2
def my_func (a):
    '''Написати функцію, яка повертає абсолютне значення числа'''
    if a >= 0:
       return a
    else:
        return -a
print (my_func(-6))

#Task 3
def find_max_of_nums (arg1, arg2):
  '''Написати функцію, яка знаходить максимальне число з двох чисел'''
  if arg1>arg2:
    print ('{} is max number'.format(arg1))
  else:
    print ('{} is max number'.format(arg2))
find_max_of_nums (48, 32)
4.  Написати програму, яка обчислює площу прямокутника, трикутника та кола (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)
def square_of_circle ():
  PI=3.14
  r=int(input("Enter radius of Circle "))
  square_circle = PI * (r * r)
  return square_circle
def square_of_triangle ():
  a=int(input("Enter lenght of Triangle's side "))
  h=int(input("Enter lenght of Triangle's height from a "))
  return 0.5*a*h
def square_of_rectangle ():
  a=int(input("Enter first side of rectangle "))
  b=int(input("Enter second side of rectangle "))
  return a*b

type_of_figure=(input("Enter square of which figure you need to count ")).upper()
if type_of_figure=="CIRCLE":
  print (square_of_circle())
elif type_of_figure=="TRIANGLE":
  print (square_of_triangle())
elif type_of_figure=="RECTANGLE":
  print (square_of_rectangle())