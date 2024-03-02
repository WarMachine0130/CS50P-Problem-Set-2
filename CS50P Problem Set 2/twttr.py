while True:
    userString = list(input('Input: '))
    
    for x in userString:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
            userString.remove(x)
    
    userString = ''.join(userString)
    print(userString)
    print('')