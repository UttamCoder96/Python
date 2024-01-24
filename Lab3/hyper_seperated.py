'''try:'''
def operation(n1):
    n2 = n1.split('-')
    #print(n2)
    for i in range(len(n2)):
        for j in range(0,len(n2)-i-1):
            if n2[j] > n2[j+1]:
                n2[j+1],n2[j] = n2[j],n2[j+1]
    print(n2)
n = 'ss-d-d-ff-htf'
operation(n)
'''except Exception as e:
    print('Error Found!')'''