from webbrowser import open as openInFolder
phone_book = dict()

def message():
    print('Do you wanna add person:(1 - add person, 2 - see a book, 0 - for exit)')

def choose():
    num = int(input())
    if num == 1:
        pers = str(input('Name = '))
        number = int(input('Number = '))
        phone_book[pers] = number
        with open('test.txt', 'w') as file:
                for items in phone_book:
                        file.writelines(str(items)+ ':')
                        file.writelines(str(phone_book[items])+'\n')

        file.close()
    elif num == 2:
        bookInfo()
    elif num == 0:
            exit()
    else:
        print('Fail option')
        message()
        choose()

def bookInfo():
    openInFolder('test.txt')

def main():
  
    while True:
        message()
        choose()

main()
