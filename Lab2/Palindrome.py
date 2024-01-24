name = (input('Enter the word or number you want: '))
name1 = name[::-1]
if name1 == name:
    print('Panlindrome')
else:
    print('Not palindrome')