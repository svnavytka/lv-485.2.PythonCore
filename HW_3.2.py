# Task 1
n = input("Enter four digit number ")
n = int(n)
 
d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10
d3 = n % 10
n = n // 10
d4 = n % 10
print("Multiply of number digits:", d1 * d2 * d3 * d4)

# Task 2
n1 = int(input("Enter four digit number : "))
n2 = 0
 
while n1 > 0:
    digit = n1 % 10; 
    n1 = n1 // 10;
    n2 = n2 * 10
    n2 = n2 + digit
 
print('Reverse number:',n2)

# Task 3
n3 = int(input("Enter four digit number : "))
s = str(n3)
print(list(s))
print(sorted(list(s)))