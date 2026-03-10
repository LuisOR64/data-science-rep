# CSV (Comma Separated Values) files

import csv

with open('new_file', 'w', newline="") as file:
    writter = csv.writer(file)
    writter.writerow(['email', 'user'])
    writter.writerow(['kana@gmail.com', 'Kana'])
    
with open('new_file', 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        # print(line)
        for item in line:
            print(item)
            