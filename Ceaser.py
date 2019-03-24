def isUpper(letter):
    if letter <= 'Z' and letter >='A':
        return True
    else:
        return False

def isLower(letter):
    if letter <= 'z' and letter >='a':
        return True
    else:
        return False


def coder(string,shift):
    stringResult = str(shift) + '\n'
    for item in string:
        Item = ord(item)
        
        if isUpper(item):
            if Item+shift > ord('Z'):
                ost = ord('Z')-Item
                Item = ord('A')+(shift-ost-1)
                stringResult+=chr(Item)
            else:
                stringResult+=chr(Item+shift)

        elif isLower(item):
            if Item+shift > ord('z'):
                ost = ord('z')-Item
                Item = ord('a')+(shift-ost-1)
                stringResult+=chr(Item)
            else:
                stringResult+=chr(Item+shift)
        else:
            stringResult+=item

    return stringResult

def decoder(string):
    iterator = 1
    num = ''
    stringResult = ''
    for letter in string:
        if letter != '\n':
            iterator+=1
            num+=letter
            shift  = int(num)
        else:
            break
    print(shift)
    new_string = string[iterator::1]
    print(new_string)


    for item in new_string:
        if isUpper(item):
            if ord(item)-shift < ord('A'):
                ost = shift-(ord(item)-ord('A'))
                Item = ord('Z')-ost+1
                stringResult+=chr(Item)
            else:
                stringResult+=chr(ord(item)-shift)
        elif isLower(item):
            if ord(item)-shift < ord('a'):
                ost = shift-(ord(item)-ord('a'))
                Item = ord('z')-ost+1
                stringResult+=chr(ord(Item))
            else:
                stringResult+=chr(ord(item)-shift)
        else:
            stringResult+=item
    return stringResult



    




string = 'XYZOP.1.abcA'
string = string.strip()
c_string = coder(string,3)
print(c_string) #ABCRS.1.defD
dc_string = decoder(c_string) 
print(dc_string)





