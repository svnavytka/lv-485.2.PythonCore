# Jenny's secret message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {}!".format(name)
a=greet(input("Enter your name "))
print(a)