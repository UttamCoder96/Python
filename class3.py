#use of 'if' and 'elif' condition
marks = input('Enter your mark: ')
if marks.isdigit():
    mark = int(marks)
    if  mark >= 80:
        print('You got first devison')
    elif  mark <80 and mark >= 32:
        print('You are pass')
    elif  mark <32:
        print('Sorry, Failed!!!')
else:
    print('Mark must be integer!!!')
#use of loop
name='Uttam Mukhiya'
for i in name:
    print(i)
    if i == 'M':
        break
    elif i == 'm':
        continue

#sorting
List = [10, 20, 3, 42,52,43]
Temp = 0
for i in List:
    if i > Temp:
        Temp = i
print(f'Greater number is: {Temp}')      
