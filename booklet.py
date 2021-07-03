def one():
    num = input('enter a whole number')
    newNum = int(num)+5
    print(newNum)

def second():
    num = input('enter a decimal or integer')
    Nnum = float(num)
    print(Nnum/2)

def third():
    age = input('enter your age: ')
    age = int(age)
    if age > 17:
        adult = True
    else:
        adult = False
def fourth():
    name = input('enter your first name')
    print(name)
    
def task18():
    num1 = int(input('enter a number: '))
    num2 = int(input('enter a number: '))
    total = num1+num2
    if total > 50:
        answer=(num1*2)*num2
        print(answer)
    else:
        answer = total * 2
        print(answer)

def task19():
    def CountNum(numm,y):
        while numm < y:
            print(numm)
            numm +=1
    def printName():
        name = input()
        print('Hello ',name)
    num = int(input('enter a number: '))
    x = 10
    if num < x:
        CountNum(num,x)
    else:
        printName()
def task25s1():
    num1 = int(input('enter a number: '))
    num2 = int(input('enter a number: '))
    total = num1 + num2
    if total >= 20 and total <=50:
        print(num1)
    else:
        print(num2)


def task25s2():
    num1 = int(input('enter a number: '))
    num2 = int(input('enter a number: '))
    num3 = int(input('enter a number: '))
    if  num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    else:
        print(num3)

def tryy():
    x = 1
    y = 2
    print(x,y)

def task25s3():
    total = 0
    num = 0
    while num != 5:
        numb = int(input('enter a number: '))
        include = input('Do you want to include this number in the total: ')
        if include == 'y' or include == 'Y':
            total += numb
        num +=1
    print(total)

def task25s4():
    total = 0
    num = int(input('enter a number '))
    while num != 7 or num < 10:
        total += num
        num = int(input('enter a number '))
    print(total)
    
def task27():
    array = []
    point = input('Enter the point: ')
    while point != 'n':
        if point == 'h':
            array.append('h')
        elif point == 't':
            array.append('t')
        else:
            print('invalid')
        point = input('Enter the point: ')
    print(array)
    
def task28():
    names = []
    u = 0
    while u != 5:
        name = input('enter a name ')
        names.append(name)
        u +=1
    print(names)
    num = int(input('enter a number: '))
    if num < 4 and num > 0:
        print(names[num])
        dorc = input('enter d if you want to delete that item, or c if you want to change it: ')
        if dorc == 'd':
            del names[num]
        elif dorc == 'c':
            del names[num]
            change = input('enter what you want to change it to: ')
            names.insert(num,change)
    print(names)

def task29():
    num1 = int(input('enter a number: '))
    num2 = int(input('enter a number: '))
    total = num1 + num2
    numbers = []
    array = [num1, num2, total]
    numbers.append(array)
    new = input('do you want to enter another row? ')
    if new == 'y':
        while new == 'y':
            num1 = int(input('enter a number: '))
            num2 = int(input('enter a number: '))
            total = num1 + num2
            array = [num1, num2, total]
            numbers.append(array)
            new = input('do you want to enter another row? ')
    print(numbers)

def task32():
    name = input('Please enter your name; ')
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a number: '))
    total = num1 + num2
    file = open('numbers.txt','a')
    endWrite = name + ':' + str(total)
    file.write(endWrite)
    file.close()

def task33():
    name1 = input('Please enter a name: ')
    num1 = int(input('Enter a number: '))
    num11 = int(input('Enter a number: '))
    name2 = input('Please enter a name: ')
    num2 = int(input('Enter a number: '))
    num22 = int(input('Enter a number: '))
    name3 = input('Please enter a name: ')
    num3 = int(input('Enter a number: '))
    num33 = int(input('Enter a number: '))
    total1 = num1 + num11
    total2 = num2 + num22
    total3 = num3 + num33
    file = open('numbers.txt','a')
    endWrite1 = name1 + ':' + str(total1)
    file.write(endWrite1)
    endWrite2 = name2 + ':' + str(total2)
    file.write(endWrite2)
    endWrite3 = name3 + ':' + str(total3)
    file.write(endWrite3)
    file.close()
def task34():
    file = open('numbers.txt','r')
    data = file.read()
    print(data)
    file.close()

def task35():
    num = float(input('Please enter a number: '))
    numm = 0
    while numm < 10:
        if int(num/2) == True:
            file = open('even.txt','a')
            file.write(str(num))
            file.close()
            numm +=1
        else:
            file = open('odd.txt','a')
            file.write(str(num))
            file.close()
            numm +=1
        num = float(input('Please enter a number: '))
    see = input('Which file do you want to see? ')
    if see.lower() == 'even':
        file = open('even.txt','r')
        data = file.read()
        print(data)
        file.close()
    elif see.lower() == 'odd':
        file = open('odd.txt','r')
        data = file.read()
        print(data)
        file.close()
    else:
        print('invalid')

def task36():
    m = input('please enter a message: ')
    l = input('please enter a letter: ')
    length = len(m)
    pos = m.find(l)
    print(m[pos:length])

def task37():
    fname = input('please enter your first name: ')
    lname = input('please enter your last name: ')
    dob = input('please enter your date of birth in the format dd/mm/yyyy: ')
    added = int(dob[0]) + int(dob[1]) + int(dob[3]) + int(dob[4]) + int(dob[6]) + int(dob[7]) + int(dob[8]) + int(dob[9])
    sur3 = lname[0:3]
    leng = len(fname)
    last = fname[leng-1]
    print(sur3 + last + str(added))

def task38():
    highnum = int(input('please enter a high number: '))
    lownum = int(input('please enter a low number: '))
    import random
    num = random.randint(lownum,highnum)
    numg = int(input('Guess the number: '))
    guesses = 0
    guesses +=1
    while numg != num:
        if numg > num:
            print('lower')
        else:
            print('higher')
        numg = int(input('Guess the number: '))
        guesses +=1
    print('well done you got it! It took you ',str(guesses),' guesses!')


def task43():
    cost=0
    pots =0
    numberofwalls=int(input("How many walls do you want me to paint?"))
    n=0
    while numberofwalls != n:
        height=int(input("Please enter the height of the wall in metres"))
        width=int(input("Please enter the width of the wall in mentres"))
        area=height*width
        import math
        pots = pots + (math.ceil(area/25)*5)
        total = math.ceil(area/10)
        cost=cost+(total*50)
        n+=1
    coats=input("Do you want two coats of paint?")
    if coats.lower()=='y':
        pots = pots * 2
    else:
        c = False
    cost = cost + pots
    print('£',cost)
    
        
def task44():
    word=input("Please enter a word")
    while len(word) < 3:
        word=input("Please enter a word")

def task45():
    name=input("Please enter your name")
    n=1
    while name==""and n<3:
         name=input("Please enter your name")
         n+=1
    if name == '':
        print('error - name not valid')
    else:
        print('good')

def task46():
    numone=int(input("Please enter a number between 1 and 100"))
    numtwo=int(input("Please enter a number between 1 and 100"))
    while numone > 100 or numone < 1:
         numone=int(input("Please enter a number between 1 and 100"))
    while numtwo > 100 or numtwo < 1:
        numtwo=int(input("Please enter a number between 1 and 100"))
    print("1.mutiply\n2.add")
    num=input("Please select an option")
    while num !='1' and num != '2':
       num=input("Please select an option")
    num=int(num)
    if num==1:
        total=numone*numtwo
        print("the answer is, ",str(total))
    else:
        total=numone+numtwo
        print("the answer is, ",str(total))

def task47():
    ID=input("Please enter a user ID")
    while len(ID) < 4:
        print("Invalid ID")
        ID=input("Please enter a user ID")
    ID=ID.lower()
    password=input("Please enter a password")
    while len(password) <8:
        print("Invalid Password")
        password=input("Please enter a password")
    file=open("passwords.txt","a")
    g = ID+'-'+password
    file.write(g)

def task48():
    n = 0
    ID=input("Please enter a user ID")
    password=input("Please enter a password")
    while n < 3:
        file=open('passwords.txt','r')
        data = file.read()
        if ID in data:
            print("Access Granted")
            break
        else:
            print("Incorrect User ID or password")
        ID=input("Please enter a user ID")
        password=input("Please enter a password")
    if n == 3:
        print('Access Denied')

def task49():
    letters=input('Enter two letters: ')
    lengthLetters=len(
        letters)
    if lengthLetters != 2:
        print('Incorrect letter choice')
    else:
        num=int(input('Enter number (0-9): '))
        if num > 0 and num < 9:
            print(letters+str(num))
        else:
            print('Incorrect number choice')


        
