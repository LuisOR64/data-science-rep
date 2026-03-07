import json
import threading

def decorator(function):
    def refunction(item={}):
        print(item)
        refunction()
        return "Kimi"
    return refunction

# def function

temp = ['kimi', 'kana', 'Kagari', 'Yui']
json = {
    'name': "Kana",
    'lang': "++",
    'days': 4561
}

temp.append('Yui++')

print(temp)
print(temp[2])
print(json['name'])
print(json)

temp.pop()
print(temp)
print(temp[1])
print(temp[-1])
print(temp[2:4])
print(temp[:])

for item in range(len(temp)):
    print('index: ', item, ' is ', temp[item])

for item in temp:
    print(item)
    
for index, item in enumerate(temp):
    print('Index ', index, ' is ', item)
    
def print_kana():
    print('Kana')

def print_kagari():
    print('Kagari')

thread = threading.Thread(target = print_kana, args=())
thread2 = threading.Thread(target = print_kagari, args=())

thread.start()
thread2.start()
print(type(thread))

temp = ('kagari', 'kana')
print(temp)
temp = list(temp)
temp.append('Kimi')
print(temp)
temp = tuple(temp)
print(temp)

print(f'''prueba {4 + 5}''')

response = None

def make_thread(function, *args):
    temp = threading.Thread(target=function, args=args)
    temp.start()

def say(mesage):
    print(str(mesage))
    global response 
    response = 'kagari'
    
make_thread(say, 'Hello Yui++')
print(response)

