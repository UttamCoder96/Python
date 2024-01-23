#sorting
l1 = [2, 7, 88, 11, 12]
l2 = sorted(l1)
print(l1, l2)
#Reverse
l1.reverse()
print(l1)
#By using -1
l3 = l1[::-1]
print(l1)
#Exception handling
try:
   l1 = [2, 7, 88, 11, 12]
   print(l1[12])
except:
   print('Out of range !!!')
#Using 'range' function
l2 = list(range(0, 7))
print(l2)
#Tuple 
'''tup = (1, 3, 6, 99)
tup.remove(3)
tup[3] = 12'''
#Counting repeated numbers
tu =(1, 3, 5, 6, 9, 88, 77, 88)
print(tu.count(88))
#Using zip method
l1 = ['U','t', 'm', 'u', 'h']
l2 = ['t', 'a', ' M', 'k', 'iya']

for i,j in zip(l1,l2):
    print(i + j, end='')
#counting
count = 0
l1 = ['uu', "UttamU", "Unknownmu"]
for i in l1:
    if len(i) >= 2 and i[0] == i[-1]:
        count+=1
print(count)
#Removing duplicate
l1 = [1,22,33,11,1,4,4,6,33,22,77,88,77,44]
l = list(set(l1))
l2 = set(l)
l3 = list(l)
print(l3)