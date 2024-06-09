for _ in range(4): print("Hello world")

print((99**3)*8)

print(5 < 3) # false
print(3 ==3) # true
print(3 == "3") # false
print("Hello" == "hello") #false
# print("3" > 3) # error

computer_brand = 'Apple'

print(f"I have an {computer_brand} computer")

name = "David"
age = 26
shoe_size = 7
info = f"I'm {name}, I'm {age} years old and wear a size {shoe_size} shoe."
print(info)

a = 13
b = 130
if a > b: 
    print("Hello World")

def oddOrEven():
    num = input("Input a number: ")
    if int(num) % 2 == 0:
        print("even")
    else: print("odd")

oddOrEven()


myName = "Good Old Mother Effing Dave"
usersName = input("Enter your name: ")
if usersName == myName: 
    print("There's clearly been a glitch in the matrix")
else: print("Oh so you're not also Good Old Mother Effing Dave? Yeah I didn't think so.")

height = input("Enter your height in cm: ")
if int(height) >= 145: 
    print("Hurry up there's a line")
else: print("I'm sorry you need to grow a few inches to ride")