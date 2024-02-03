import pandas as pd
list1 = ['Uttam', 20,'mukhiya' ]
a = pd.Series(list1)
dict1 = {1: 'Uttam', 2:'Pragyan'}
b = pd.Series(dict1)
list2 = [['Uttam', 20, 'ilam'] ,['Pragyan', 20, 'dang']]
c = pd.DataFrame(list2, columns = ['name', 'age', 'address'])
print(a)
print(b)
print(c)