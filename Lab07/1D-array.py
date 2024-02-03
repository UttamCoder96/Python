import numpy as np 
array1 = np.arange(0,9)
# print(array1)

#10 * 10 array
array2 = np.arange(0,100).reshape(10,10)
# print(array2)
# print(np.max(array2))
# print(np.min(array2))

#dot product
array3 = np.arange(1,10).reshape(3,3)
array4 = np.arange(10,19).reshape(3,3)
#print(np.arange(10,19)@np.arange(1,10))

#random module in numpy
array5 = np.random.randint(1,11,(2,5))
#print(array5)

#2D array
#sum
array6 = array3 + array3
#print(array6)

#multiply
array7 = array3 * array3
# print(array7)

#log
# print(np.log(array3))

#exponental
# print(np.exp(array3))

#log`10`
# print(np.log10(array3))

#standard division
# print(np.std(array3))

#correlation
# print(np.corrcoef(array3))

#transpose
array8 = np.arange(10,26).reshape(4,4)
# print(np.transpose(array8))

#user input matrix
n1 = int(input('Enter the size of row of matrix: '))
n2 = int(input('Enter the size of column of matrix: '))
l1 = []
for i in range(0,n1):
    for j in range(1,n2+1):
        num2 = int(input(f'Enter the value of [{i}][{j}]: '))
        l1.append(num2)
print(np.array(l1).reshape(n1,n2))
