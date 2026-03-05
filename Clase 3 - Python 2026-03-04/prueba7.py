def clear():
    print("\033c", end="")
        
def pause():
    input("Presione cualquier tecla para continuar...")

def menu():
    print("=============================================")
    print("          CONVERTIDOR DE MONEDAS             ")
    print("=============================================")
    print("     [1] CONVERTIR SOLES A DOLARES           ")
    print("     [2] CONVERTIR DOLARES A SOLES           ")
    print("     [3] SALIR                               ")
    print("=============================================")
    
def end():
    option = input("Esta seguro que desea salir? (Y/N): ")
    return "Y" if option.upper() == "Y" else "N"
    
def operator(operator):
    num = int(input("Escriba la cantidad a convertir: "))
    if operator == 1:
        print("S/." + str(num) + " equivale a $" + str(num/3))
    elif operator == 2:
        print("$" + str(num) + " equivale a S/." + str(num*3))
    pause()
    
def run():
    while 1==1:
        clear()
        menu()
        option = int(input("Escriba una opcion: "))
        if option >= 1 and option <= 3:
            if(option == 3):
                resp = end()
                exit() if resp == "Y" else None
            else:
                operator(option)
        else:
            print("Opcion no válida")
        
run()
clear()