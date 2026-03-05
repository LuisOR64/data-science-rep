import os

num = 0
num2 = 0
option=0

def menu():
    print("Calculadora")
    print("====================")
    print("(1) => Suma")
    print("(2) => Resta")
    print("(3) => Multiplicación")
    print("(4) => División")
    print("(5) => Cerrar")
    
def pause():
    input("Press any key to continue...")
    
def clear():
    print("\033c", end="")
    
def calculate(operator):
    global num, num2
    num = int(input("Type fisrt number: "))
    num2 = int(input("Type second number: "))
    
    if operator == 1:
        print("Response: " + str(num + num2))
    else: 
        if operator == 2:
            print("Response: " + str(num - num2))
        else:
            if operator == 3:
                print("Response: " + str(num * num2))
            else:
                if operator == 4:
                    print("Response: " + str(num / num2))
    pause()
    
def run():
    global option
    while option != 3:
        clear()
        menu()
        option = int(input("Type option: "))
        
        if option >= 1 and option <= 4:
            calculate(option)
        else:
            if option == 5:
                exit()
            else:
                print("Option incorrect, try again")
                pause()
            
run()
clear()