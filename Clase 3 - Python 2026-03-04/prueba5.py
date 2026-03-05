import random

def mesage():
    print("Try to adivinate the number")

def again(tip):
    print("Try again, try " + tip)

num = random.randint(1, 10)

while 1==1:
    mesage()
    num2 = int(input("Type a number: "))
    if(num != num2):
        again( str("lower" if num2 > num else "upper") )
    else:
        print("You win")
        exit()