
temp=[]
max=0
min=0

def ordenar(numbers):
    temp=0
    for index, item in enumerate(numbers):
        for index2, item2 in enumerate(numbers):
            if item > item2:
                temp = item2
                numbers[index2]=numbers[index]
                numbers[index]=temp
                
                # numbers[index], numbers[index2] = numbers[index2], numbers[index]
    
    print(numbers)                
                
        
print('Ingrese 5 numeros: ')
for item in range(5):
    temp.append(int(input(f'''Ingrese el numero {item+1}: ''')))
    
print("====================")
print("""La lista es:""")

max=min=temp[0]

for index, item in enumerate(temp):
    max = item if max < item else max
    min = item if min > item else min
    print(f'''El item Nº{index} es: {item}''')
    
print(f"El numero mayor es: {max}")
print(f"El numero menor es: {min}")
print(f"La lista ordenada es: ")
ordenar(temp)



    
    
