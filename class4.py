#1
n =1 
while n <= 10:
    print(n)
    n+=1

#2
N = int(input('Enter any integer: '))
sum = 0
for i in range(1, N+1):
    sum+=i
print(f'Sum= {sum}')
#Multiplication table
n = int(input('Enter any integer:'))
mul = 1
for i in range(1, 11):
    mul = n*i
    print(mul)
#Reverse integer
number = input('Enter any integer: ')
print(number[ : : -1])
#check same values
num1 = int(input('Enter length: '))
num2 = int(input('Enter breadth: '))
if num1 == num2:
    print('It is square')
else:
    print('It is rectangle')
#finding greatest value
num1 = int(input('Enter first integer: '))
num2 = int(input('Enter second integer: '))
if num1 > num2:
    print(f'The greater value is: {num1}')
if num1 < num2:
    print(f'Greater value is: {num2}')
if num1 == num2:
    print('They are equal')
#age compare
age1 = int(input('Enter first person age: '))
age2 = int(input('Enter second person age: '))
age3 = int(input('Enter third peraon age: '))
List = [age1, age2, age3]
temp =  0
for i in List:
    if i > temp:
        temp = i
if temp == age1:
    print('First person is oldest')
elif temp == age2:
    print('Second person is oldest')
elif temp == age3:
    print('Third person is oldest')
#triangle pattren
num = int(input('Enter any number: '))
for i in range(1, num+1):
    for j in range(1, i+1):
        print('*', end='')
    print('\n')
#split
name = 'Ramayan'
name1 = [12, 43, 5, 66, 1]
print('splitting by a')
print(name.split('a'))
name1.append(17)
print('adding element at the last of list')
name1.insert(2, 1000)
print('inserting 1000 at first position of list')
name1.remove(43)
print('Removing 43 from list')
print(name1)
name1.sort(reverse=False)
print('Sorting list in decending ascending')
print(name1)
name1.extend(name)
print('Extending name1 and name')
print(name1)
name = name1.copy()
print(name)