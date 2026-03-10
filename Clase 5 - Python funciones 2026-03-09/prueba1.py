import os

temp = {}

def clear():
    print("\033c", end="")
    
def pause():
    input("Presione cualquier tecla para continuar...")

def end():
    exit()

def up_operator(option, key, item):
    temp2 = ''
    clear()
    print('Actualización de datos')
    if option == 1:
        
        temp2 = data_control('Ingrese en nuevo DNI: ')
        temp[temp2] = temp.pop(key)
        key = temp2
        print('Se realizaó la actualización satisfactoriamente')
        
    elif option == 2:
        
        temp[key]['name'] = data_control('Ingrese en nuevo Nombre: ')
        print('Se realizaó la actualización satisfactoriamente')
        
    elif option == 3:
        
        temp[key]['email'] = data_control('Ingrese en nuevo Email: ')
        print('Se realizaó la actualización satisfactoriamente')
        
    elif option == 4:
        
        temp2 = data_control('Ingrese en nuevo DNI: ')
        temp.pop(key)
        temp[temp2] = { 'name' : data_control('Ingrese el nuevo Nombre: '), 'email': data_control('Ingrese el nuevo Email: ')}
        key = temp2
        item = temp[key]
        print('Se realizaó la actualización satisfactoriamente')
    
    pause() 
    return key, item
    # clear()

def update_menu(key, item):
    control = True
    
    while control == True:
        print("""¿Cómo desea realizar la actualización?""")
        print(f"""(1)       Actualizar DNI [{ key }]""")
        print(f"""(2)       Actualizar Nombre [{ item['name'] }]""")
        print(f"""(3)       Actualizar Email [{ item['email'] }]""")
        print(f"""(4)       Actualizar Todo""")
        print(f"""(C)               Cancelar""")
        print("""=======================================""")
    
        option = str(input('Ingrese una opción: ')).rstrip()
    
        if option.isdigit() == False:
            if option.upper() == 'C':
                control = False
            else:
                print('Opción no válida')
        elif 1 <= int(option) <= 4:
            key, item = up_operator(int(option), key, item)
        else:
            print('Opción no válida')
        clear()

def data_control(mesage):
    response = ''
    cont = 0
    while response.rstrip() == '':
        if cont > 0:
            clear()
            print('¡Debe ingresar la información solicitada!')
        response = str(input(mesage))
        cont += 1
    return response 
        

def print_item(key, item):

    print(f'''Información encontrada:''')
    print(f'''DNI: {key}''')
    print(f'''Nombre: {item['name']}''')
    print(f'''Email: {item['email']}''')

def operate(option):
    clear()
    control = True
    temp2 = ''
    temp3 = ''
    if option == 1:
        
        print(f"""Ingrese la información según de valla solicitando""")
        # dni = str(input('Ingrese el DNI: '))
        dni = data_control('Ingrese el DNI: ')
        temp[dni] = { 'name' : data_control('Ingrese el nombre: '), 'email': data_control('Ingrese el email: ')}
        # temp[dni] = { 'name' : str(input('Ingrese el nombre: ')), 'email': str(input('Ingrese el email: '))}
        print(f"""Registro completo""")
        
    elif option == 2:
        
        print(f"""Impresión de datos""")
        temp2 = data_control('Escriba el DNI a consultar: ')
        print_item(temp2, temp[temp2]) if temp.get(temp2) else print('No se encontro la información solicitada')
        
    elif option == 3:
        
        print(f"""Actualización de datos""")
        temp2 = data_control('Escriba el DNI a Actualizar: ')
        temp3 = temp.get(temp2)
        if temp3:
            # control = True
            # while control == True:
            clear()
            update_menu(temp2, temp3)
            # pause()
            # clear()
            
        else:
            print('No se encontro la información solicitada')
        
    elif option == 4:
        
        print(f"""Eliminación de datos""")
        temp2 = temp.pop(data_control('Escriba el DNI a eliminar: '), None)
        print('Se ha eliminado el registro') if temp2 else print('No se encontro el registro solicitado')
        
    elif option == 5:
        
        print(f"""Impresión de datos""")
        
        for index, (key, item) in enumerate(temp.items()):
            print(f"""{"="*5}Registro Nº {index+1}{"="*5}""")
            print(f'''DNI: {key}''')
            print(f'''Nombre: {item['name']}''')
            print(f'''Email: {item['email']}''')
            
        print(f"""===================""")

def menu():
    print('''
          =========SQL_PY===========
          (1)         Nuevo registro
          (2)      Imprimir registro
          (3)    Actualizar Registro
          (4)      Eliminar Registro
          (5)          Imprimir Todo     
          (C)         Cerrar Sistema
          ==========================
          ''')
    option = str(input('Ingrese una opción: ')).rstrip()
    
    if option.isdigit() == False:
        if option.upper() == 'C':
            clear()
            exit()
        else:
            print('Opción no válida')
    elif 1 <= int(option) <= 5:
        operate(int(option))
    else:
        print('Opción no válida')
    
def run():
    while True:
        clear()
        menu()
        pause()
        
run()
