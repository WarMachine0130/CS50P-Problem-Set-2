import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = list(s)
    
    for x in range(len(s)):
        if s[x].isalpha() != True or s[x + 1].isalpha() != True:
            return False
        elif len(s) < 2 or len(s) > 6:
            return False
        elif s[x] in string.punctuation:
            return False
        else:
            return True

while True:
    main()
    print('')