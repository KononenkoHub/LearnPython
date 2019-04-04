class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)



def checkBracketsForClosing(ch1,ch2):
    if ch1 == '(' and ch2 == ')':
        return True
    elif ch1 == '{' and ch2 == '}':
        return True
    elif ch1 == '[' and ch2 == ']':
        return True
    else:
        return False

def bracketsIsOpen(ch):
    if ch == '{' or ch =='[' or ch == '(':
        return True
    else:
        return False

def bracketsIsClose(ch):
    if ch == '}' or ch ==']' or ch == ')':
        return True
    else:
        return False

def checkString(string):
    s = Stack()
    for element in string:
        if bracketsIsOpen(element):
            s.push(element)
        elif bracketsIsClose(element):
            if s.size() == 0:
                return False
            if checkBracketsForClosing(s.peek(),element):
                s.pop()
            else:
                return False
    
    if s.size() !=0:
        return False
    else:
        return True
        



string = str(input('Enter a string = '))
print(checkString(string))