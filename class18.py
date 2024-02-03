#file
#open('file_name.ext','mode')
#write mode

f = open('class18.txt', 'w')
f.write('This is added text')
f.close()
#read mode
f = open('class18.txt', 'r')
data = f.read()
print(data)
f.close()
#write read mode
f = open('class18.txt', 'w+')
f.write('This is added.')
print(f.tell())
sata = f.read()
print(sata)
f.close()
#for seek()
f = open('class18.txt', 'r')
print(f.tell())
f.seek(4)
print(f.tell())
#rename file
import os
f = open('class18.txt', 'w+')
f.close()
os.rename('class17.txt', 'class18.txt')
#writing list on file
li = ['Uttam', 'Pragyan']
with open('class18.txt', 'w') as f:
    f.writelines(li)



