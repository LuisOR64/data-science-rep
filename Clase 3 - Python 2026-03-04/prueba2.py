import os

temp = int(45)
temp2 = str("45")

num = 0
num2 = 0
option=0

def menu():
    print("Calculadora")
    print("(1) => Suma")
    print("(2) => Resta")
    print("(3) => Close")
    
def sum():
    global num
    global num2
    
    num = int(input("Type fisrt number: "))
    num2 = int(input("Type second number: "))
    
    print("Response: " + str(num + num2) + ", is an " + str(type(num + num2)))
    #os.system("pause")
    input("Press any key to continue...")
    
def subs():
    global num
    global num2
    
    num = int(input("Type fisrt number: "))
    num2 = int(input("Type second number: "))
    
    print("Response: " + str(num - num2) + ", is an " + str(type(num - num2)))
    #os.system("pause")
    input("Press any key to continue...")
    
def run():
    global option
    while option != 3:
        # os.system("cls")
        print("\033c", end="")
        menu()
        option = int(input("Type option: "))
        if option == 1:
            sum()
        if option == 2:
            subs()
            
run()
print("\033c", end="")