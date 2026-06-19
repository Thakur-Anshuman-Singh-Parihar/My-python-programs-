import math
def D2B(num):
    Decimal = num
    binary = 0
    x = 1
    for i in range (num + 1):
        if num == 0 :
            break
        elif num > 0 :
            a = num % 2 
            b = num//2
            binary = binary + a*x
            x = x*10
            num = b
    print("\n  Decimal           Binary")
    print("-"*40)
    print(f"  {Decimal}        =       {binary}\n\n")

def B2D(num):
    binary = num
    dec = 0
    power = 0
    for i in range(20):
        n = num % 10
        num = num // 10
        dec = dec + n * math.pow(2,power)
        power = power + 1
    print("\n  Binary           Decimel")
    print("-"*40)
    print(f"  {binary}        =       {dec}\n\n")

def D2O(num):
    Decimal = num
    Octel = 0
    x = 1
    for i in range (num + 1):
        if num == 0 :
            break
        elif num > 0 :
            a = num % 8 
            b = num//8
            Octel = Octel + a*x
            x = x*10
            num = b
    print("\n  Decimal           Octel")
    print("-"*40)
    print(f"  {Decimal}        =       {Octel}\n\n")

def O2D(num):
    Octel = num
    dec = 0
    power = 0
    for i in range(20):
        n = num % 10
        num = num // 10
        dec = dec + n * math.pow(8,power)
        power = power + 1
    print("\n  Octel           Decimel")
    print("-"*40)
    print(f"  {Octel}        =       {dec}\n\n")

def D2H(num):
    Decimal = num
    Hexa = ''
    x = 1
    for i in range (num + 1):
        if num == 0 :
            break
        elif num > 0 :
            a = num % 16 
            b = num//16
            a = str(a)
            if a == '10':
                a = 'A'
            elif a == '11':
                a = 'B'
            elif a == '12':
                a = 'C'
            elif a == '13':
                a = 'D'
            elif a == '14':
                a = 'E'
            elif a == '15':
                a = 'F'
            Hexa = a + Hexa
            a = 0
            num = b
    print("\n  Decimal           Hexadecimal")
    print("-"*40)
    print(f"  {Decimal}        =       {Hexa}\n\n")

def H2D(num):
    Hexa = num
    dec = 0
    power = 0
    for i in range(len(Hexa)):
        a = Hexa[len(Hexa)-(i+1)]
        if a == 'A':
            a = '10'
        elif a == 'B':
            a = '11'
        elif a == 'C':
            a = '12'
        elif a == 'D':
            a = '13'
        elif a == 'E':
            a = '14'
        elif a == 'F':
            a = '15'
        a = int(a)
        dec = dec + a * math.pow(16,power)
        power = power + 1
    print("\n  Hexadecimal           Decimel")
    print("-"*40)
    print(f"  {Hexa}        =       {dec}\n\n")

print("\n                   Welcome To Base Converter\n","="*70,"\n")
for i in range (100):
    print("   1 .    Decimal   -->   Binary   \n   2 .    Binary   -->   Decimal   \n   3 .    Decimal   -->   Octel   \n"\
           "   4 .    Octel   -->   Decimal   \n   5 .    Decimal   -->   Hexadecimal   \n   6 .    Hexadecimal   -->   Decimal   \n ")
    op = int(input("  Choose option according to your need ___.....  "))
    if op == 1:
        num = int (input("\n  Enter your decimal number :  "))
        D2B(num)
    elif op == 2 :
        num = int (input("\n  Enter your binary number :  "))
        s = num
        for i in range(20):
            a = s % 10
            s = s//10
            if a != 0 and a != 1 :
                print("\n  Please Enter A Valid Binary Number Like ...   1011101  ,  1101  ,  1111111.....\n")
                break
        else:
            B2D(num)
    elif op == 3 :
        num = int (input("\n  Enter your decimal number :  "))
        D2O(num)
    elif op == 4 :
        num = int (input("\n  Enter your octel number :  "))
        s = num
        for i in range(20):
            a = s % 10
            s = s//10
            if a == 8 or a == 9 :
                print("\n  Please Enter A Valid Octel Number Like ...   17747  ,  12342  ,  4567777 .....\n")
                break
        else:
            B2D(num)
        O2D(num)
    elif op == 5:
        num = int (input("\n  Enter your decimal number :  "))
        D2H(num)
    elif op == 6 :
        num = input("\n  Enter your hexadecimal number :  ").upper()
        invalid = "GHIJKLMNOPQRSTUVWXYZ"
        a = True
        for i in range (len(num)):
            for j in range (20):
                if num[i] == invalid[j]:
                    print("\n  Please Enter A Valid Hexadecimal Number , It is a combination of 1-9 and A-E .\n")
                    a = False
                    break
        if a == True:   
            H2D(num)
    else:
        print("\nInvalid option.....\n")
