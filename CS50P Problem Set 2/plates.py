import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = list(s)
    
    if len(s) < 4:
        #print('failed not enough letters')
        return False
    
    if s[0].isalpha() != True or s[1].isalpha() != True:
            #print('failed first two letters alphabet')
            #print(f'{s[x]} {s[x + 1]}')
            return False

    for x in range(len(s)):
        if len(s) < 2 or len(s) > 6:
            #print('failed length')
            return False
        elif s[x] in string.punctuation:
            #print('failed Punctuation')
            return False

    for x in s:
        if x in '1234567890':
            numEnd = True
        else:
            numEnd = False
            
    if numEnd == False:
        #print('failed end number')
        return False

    s.reverse()
    
    endNumbers = []
    for x in s:
        if x in '1234567890':
            endNumbers.append(x)
        else:
            break

    endNumbers.reverse()
    
    if endNumbers[0] == '0':
        #print('failed start with not 0')
        return False
              
    return True

while True:
    main()
    print('')