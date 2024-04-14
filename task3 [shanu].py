bnr = '''
▀▀█▀▀ █▀▀█ █▀▀ █ ▄▀           █▀▀█ 
  █   █▄▄█ ▀▀█ █▀▄   ▀▀         ▀▄ 
  ▀   ▀  ▀ ▀▀▀ ▀  ▀           █▄▄█
\n'''
print("\033[96m" + bnr + "\033[0m") 


def fact(n):
    return 1 if n == 0 else n * fact(n - 1)

while(True):
    try:
        n=abs(int(input("Enter number to take Factorial :")))
        res= fact(n)
        print(f'\033[32mFactorial :{res} \033[0m')
        break
    except:
        print('\033[31m Invalid Entry.\033[0m')
while(True):
    try:
        txt=input('Enter the text to count :')
        s=c=t=0
        for x in txt:
            if x.isupper():
                c=c+1
            elif x.islower():
                s=s+1
            else:
                t=t+1
        print(f'''The String you gave has
                Capital letters : \033[32m {c}\033[0m
                Small letters   : \033[32m {s}\033[0m
                Other Entries   : \033[32m {t}\033[0m
                ''')
        break
    except:
        print('\033[31m Invalid Entry.\033[0m')
while(True):
    try:
        txt=input('Enter String : \033[32meg helo-abc-def \033[0m')
        txt=txt.split('-')
        txt=sorted(txt)
        txt='-'.join(txt)
        print(f'The String you gave me is sorted :\n\t\t\t\033[032m{txt} \033[0m')
        break
    except:
        print('\033[31m Invalid Entry.\033[0m')

l=[]
while(True):
    try:
        e=input('Enter elemets of list :')
        if(e=='x'):
            break
        e=int(e)
        l.append(e)
        sq=list(map(lambda x: x * x, l))
        cb=list(map(lambda x: x*x*x, l))
    except:
        print('\033[31m Invalid Entry.\033[0m')
    finally:
        print('\033[32mPress x to exit when done.\033[0m')
print('4.The List  we are using\t\t:'+"\033[96m" + str(l) + "\033[0m")
print('\t\tSquared Lust \t\t:'+"\033[96m" + str(sq) + "\033[0m")
print('\t\tCube of List\t\t:'+"\033[96m" + str(cb) + "\033[0m")
check=lambda s,e:s.startswith(e)
while(True):
    try:
        s=input('Enter String to check:')
        e=input('enter character to check:')
        if(check(s,e)):
            print(f'\033[32mYes ,it start with the given character({e})\033[0m')
        else:
            print('\033[31mNo, the string you gave me doesn`t start with this character\033[0m')
        break
    except:
        print('\033[31m Invalid Entry.\033[0m')
        break