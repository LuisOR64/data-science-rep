import re
import time

def read(message):
    if "Kanna comand" in message:
        print('Write a command')
        

def say_something(message):
    print(message)
    
def command():
    comand = str(input('console: ')).strip()
    
    if "say" in comand.strip().lower():
        # print(comand.rstrip().lower().replace("say", ""))
        say_something(re.sub("say", "", comand, flags=re.IGNORECASE).strip())
        
# command()    

def print_collection(*items):
    for index, item in enumerate(items):
        print(f'item Nº{index} : {item}')
        
        
print_collection('Kimi', 'Kagari', 'Yui')

def print_collection2(**collec):
    for index, item in collec.items():
        print(f'{index} : {item}')
        # print(item.keys())
        # print(item.values())
        
print_collection2(kimi=2, kagari=3, kana=4)

def print_a_b(a=45, b=78):
    def plus():
        print(a+b)
    def mult():
        print(a*b)

    plus()
    mult()
    
    
def time_meter(function):
    def meter(item):
        start = time.time()
        temp = function(item)
        end = time.time()
        # start = end - start
        print(f'time: { end - start }')
        return temp
    return meter
    
@time_meter
def plus_collect(item):
    num = 0
    if len(item) > 1:
        # num = num + plus_collect(item.pop())
        return item
    # else:
        # return item
    
# def plus_collect2(item):
#     num = 0
#     if len(item) > 1:
#         num = item.pop()
#         return num
#     else:
#         return item
    
print_something2 = lambda item: print(item)

print_something2('Kimi ni todoke')

print_a_b()

print(plus_collect([1,2,3,4]))
# print(len([1,2,3,4]))
# time_meter(plus_collect([1,2,3,4]))
