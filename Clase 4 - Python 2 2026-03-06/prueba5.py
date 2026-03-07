temp = {
    'name': 'Kimi',
    'ver': 478,
    'channel': 78
}

for index, item in temp.items():
    print(f'''index: {index}, value: {item}''')
    
temp['new'] = 'Kana'

print(temp)
print(temp.pop('cc', '''Don't exist'''))

print('Kana' if 'name' in temp else '')
print('Kana' if 'Kimi' in temp.keys() else '')
print('Kana' if 'Kimi' in temp.values() else '')
print('Kana' if 'Kimi' in list(temp.items()) else '')
print(list(temp.items()))
print(temp.items())
