import sys

temp = "kimi"
temp2 = "Kana"
temp3 = None
temp4 = ['sad', 45, 'kimi']
temp5 = input("type a number: ")

def changeValue():
    global temp2
    temp2 = "Kagari"

changeValue()
print(temp.rstrip())
print("first", "second")
print(sys.version)
print(temp2)
print(temp3)
print(temp4)
print(type(temp4))
print(temp5)