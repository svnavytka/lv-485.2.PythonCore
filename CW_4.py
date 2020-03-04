#Task 1 Which value is bigger

a=int(input("Enter first number "))
b=int(input("Enter second number "))
if a>b:
    print('First value is more then Second')
else:
   print('Second value is more then First')   
#Task 2 Even or Odd value

z=int(input("Enter any number "))
if z%2==0:
   print ("Even number")
else:
   print ("Odd number")
#Task 3 Factorial

n=int(input("Enter number that you need to find factorial for "))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)
#Task 4.1 Print all even values less than 100

start=0
finish=100
while start<finish: 
    if start % 2 == 0:
        print(start)
    start+=1
else:
   print ('The end')
#Task 4.2 Print all even values less than 100

for a in range(0, 101, 2):
    print(a, end=" ")
#Task 5.1 Print all odd values less than 100

for a in range(1, 101, 2):
    print(a, end=" ")
    #Task 5.2 Print all odd values less than 100

for a in range(0, 101):
    if a % 2 == 0:
        continue
    print(a, end=" ")
#Task 6 Check list for odd values NEED HELP TO FIX IT!!!

ccc=[10, 4, 2]
for a in ccc:
    if a % 2 != 0:
        break
    else:
        print("List contains even values only")
print("List contains odd values, such as", a)

#Task 7 Change values in list to float

a = [9, 34, 26, 55, 65, 13]
pos = 0
for x in a:
    a[pos] = float(a[pos])
    pos += 1
print(a)
#Task 8

fib1 = fib2 = 1
n = int(input("Enter number of positions Fibo list: ")) - 2
 
while n > 0:
    print(fib1, end=" ")
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1
 
print(': It is your Fibo list')