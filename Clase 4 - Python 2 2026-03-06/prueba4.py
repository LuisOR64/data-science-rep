temp=[]
  
print('Ingrese 5 numeros: ')
for item in range(5):
    temp.append(int(input(f'''Ingrese el numero {item+1}: ''')))
    
print("====================")
print("""La lista es:""")

for index, item in enumerate(temp):
    print(f'''El item Nº{index} es: {item}''')
    
print(f"El numero mayor es: {max(temp)}")
print(f"El numero menor es: {min(temp)}")
print(f"La lista ordenada es: ")
# temp.sort()
# print(temp)
temp.sort(reverse=True)
print(temp)

