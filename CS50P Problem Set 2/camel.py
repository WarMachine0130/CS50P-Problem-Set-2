while True:
    
    userVar = list(input('camelCase: '))
    
    for x in range(len(userVar)):
        if userVar[x] == '_':
            userVar[x + 1] = userVar[x + 1].upper()
            
    for x in userVar:
        if x == '_':
            userVar.remove(x)
            
    userVar = ''.join(userVar)
    print(userVar)
            
            