#List comprehensive 
l1 = [2, 4, 6, 8]
l2 = [i**2 for i in l1]
print(l2)
#Set
l1 = {True, 0, 2, 4, 5, 7, 1}
print(l1)
l1.add(90)
print(l1)
#Converting tuple to string
l1 = (1, 2, 3, 5, 7)
strn= ''
for i in l1:
    if isinstance(i, str):
        strn += 1
    else:
        strn += str(i)
print(strn)
#Joining
tup = (1,4,7,8)
name = ''.join(str(tup))
print(name)
#Finding 2nd element from last
l1 = (1, 3, 5, 44, 55, 7)
l2 = len(l1)
print(l1[l2-2])
#Check element in tuple
tup = ('U', 't', 'a', 'm')
if 'U' in tup:
    print('Found')
else:
    print('Not found')
    #removing the last item of tuple from list
l1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
l2 = []
for i in l1:
    t1 = list(i)
    t1.remove(t1[-1])
    l2.append(tuple(t1))
print(l2)