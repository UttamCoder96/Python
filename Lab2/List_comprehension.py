try:
    l1 = [3, 6, 9, 12]
    l2 = [i **2 for i in l1]
    print(l2)
except ValueError as v:
    print('Invalid !!')