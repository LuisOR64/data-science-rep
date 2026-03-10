
# w => escritura
# r => lectura
# a => añadir texto

with open('temp.txt', 'w') as file:
    file.write("Hello Yui++ \n")
    file.write("Kagari")
    
with open('temp.txt', 'r') as file:
    for item in file:
        print(item.strip())
        
with open('temp.txt', 'r') as file:
    temp = file.read()
    print(temp)
    
with open('temp.txt', 'a') as file:
    new_line = str(input('Write a new line: '))
    file.write('\n')
    file.write(new_line)