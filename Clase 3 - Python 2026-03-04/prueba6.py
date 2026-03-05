
import math

def menu():
    print("Calculadora")
    print("====================")
    print("(1) => Suma")
    print("(2) => Resta")
    print("(3) => Multiplicación")
    print("(4) => División")
    print("(5) => Raiz Cuadrada")
    print("(6) => Cerrar")
    
def pause():
    input("Press any key to continue...")
    
def clear():
    print("\033c", end="")
    
def calculate(operator):
    num = int(input("Type fisrt number: "))
    
    if operator != 5:
        num2 = int(input("Type second number: "))
    
    if operator == 1:
        print("Response: " + str(num + num2))
    elif operator == 2:
        print("Response: " + str(num - num2))
    elif operator == 3:
        print("Response: " + str(num * num2))
    elif operator == 4:
        print("Response: " + str(num / num2))
    elif operator == 5:
        print("Response: " + str( math.sqrt(num) ))
    
    pause()
    
def end():
    option = input("Are you shure to close? (Y/N): ")
    if(option.upper() == "Y"):
        return 6
    return 0
    
def run():
    option = 0
    while option != 6:
        clear()
        menu()
        option = int(input("Type option: "))
        
        if option == 6:
           option = end()  
        
        if option >= 1 and option <= 5:
            calculate(option)
        else:
            print("Option incorrect, try again")
            pause()
            
run()
clear()