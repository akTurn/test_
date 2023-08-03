print("Welcome to Python – It is a great language!!!")

if True:
 print("True")
else:
 print("False")

#\n While the below is error

if True:
    print("Answer")
    print("True" )
else:
 print("Answer")
 print("False")


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)


import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check(email):

    if(re.search(regex,email)):
        print("Valid Email")
    else:
        print("Invalid Email")

if __name__ == '__main__' :

    email = "praveen@c-sharpcorner.com"
    check(email)

    email = "inform2atul@gmail.com"
    check(email)


a = int(input("What is your age? "))
print("In Eight years from now , you will be", a + 8, "years old!")
print("In ten years from now , you will be", a + 10, "years old!")
print("In twenty Four years from now , you will be", a + 24, "years old!")






import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')
