# More than 500 Lines of code , Don't dare read this just run it!😛
bnr = '''
▀▀█▀▀ █▀▀█ █▀▀ █ ▄▀        █▀█ 
  █   █▄▄█ ▀▀█ █▀▄   ▀▀     ▄▀ 
  ▀   ▀  ▀ ▀▀▀ ▀  ▀        █▄▄\n'''
print("\033[96m" + bnr + "\033[0m") 
# Functions:
def Sopts():
    print('capitalize()\t\t:', "\033[31m" + my_str.capitalize() + "\033[0m")
    print('casefold()\t\t:', "\033[31m" + my_str.casefold() + "\033[0m")
    print('center()\t\t:', "\033[31m" + my_str.center(20) + "\033[0m")
    print('count()\t\t\t:', "\033[31m" + str(my_str.count('i')) + "\033[0m")
    print('encode()\t\t:',  my_str.encode())
    print('endswith()\t\t:', "\033[31m" + str(my_str.endswith('world')) + "\033[0m")
    print('expandtabs()\t\t:', "\033[31m" + my_str.expandtabs(4) + "\033[0m")
    print('find()\t\t\t:', "\033[31m" + str(my_str.find('i')) + "\033[0m")
    print('format()\t\t:', "\033[31m" + "nyctophile".format() + "\033[0m")
    print('format_map()\t\t:', "\033[31m" + "nyctophile".format_map({'k1': 'v1'}) + "\033[0m")
    print('index()\t\t\t:', "\033[31m" + str(my_str.index('i')) + "\033[0m")
    print('isalnum()\t\t:', "\033[31m" + str(my_str.isalnum()) + "\033[0m")
    print('isalpha()\t\t:', "\033[31m" + str(my_str.isalpha()) + "\033[0m")
    print('isdecimal()\t\t:', "\033[31m" + str(my_str.isdecimal()) + "\033[0m")
    print('isdigit()\t\t:', "\033[31m" + str(my_str.isdigit()) + "\033[0m")
    print('isidentifier()\t\t:', "\033[31m" + str(my_str.isidentifier()) + "\033[0m")
    print('islower()\t\t:', "\033[31m" + str(my_str.islower()) + "\033[0m")
    print('isnumeric()\t\t:', "\033[31m" + str(my_str.isnumeric()) + "\033[0m")
    print('isprintable()\t\t:', "\033[31m" + str(my_str.isprintable()) + "\033[0m")
    print('isspace()\t\t:', "\033[31m" + str(my_str.isspace()) + "\033[0m")
    print('istitle()\t\t:', "\033[31m" + str(my_str.istitle()) + "\033[0m")
    print('isupper()\t\t:', "\033[31m" + str(my_str.isupper()) + "\033[0m")
    print('join()\t\t\t:', "\033[31m" +'123'.join('456') + "\033[0m")
    print('lower()\t\t\t:', "\033[31m" + my_str.lower() + "\033[0m")
    print('maketrans()\t\t:', "\033[31m" + str(my_str.maketrans('abc', '123')) + "\033[0m")
    print('partition()\t\t:', "\033[31m" + str(my_str.partition(' ')) + "\033[0m")
    print('replace()\t\t:', "\033[31m" + my_str.replace('my', 'pulic') + "\033[0m")
    print('split()\t\t\t:', "\033[31m" + str(my_str.split()) + "\033[0m")
    print('splitlines()\t\t:', "\033[31m" + str(my_str.splitlines()) + "\033[0m")
    print('startswith()\t\t:', "\033[31m" + str(my_str.startswith('this')) + "\033[0m")
    print('strip()\t\t\t:', "\033[31m" + my_str.strip() + "\033[0m")
    print('swapcase()\t\t:', "\033[31m" + my_str.swapcase() + "\033[0m")
    print('title()\t\t\t:', "\033[31m" + my_str.title() + "\033[0m")
    print('translate()\t\t:', "\033[31m" + str(my_str.translate({104: 105})) + "\033[0m")
    print('upper()\t\t\t:', "\033[31m" + my_str.upper() + "\033[0m")
    print('zfill()\t\t\t:', "\033[31m" + my_str.zfill(15) + "\033[0m")
def Sdefs():
    print(''' 
    This is from Chat gpt ,
     since i was not familiar with all these operations ,
     i used this as a refrence & also giving it here.

        1. `capitalize()`: Converts the first character of the string to uppercase
         and converts all other characters to lowercase.

        2. `casefold()`: Similar to `lower()`, but more aggressive.
         It converts the string to lowercase and also handles special cases such as German's ß.

        3. `center(width, fillchar)`: Returns a centered string of length `width`.
         The original string is centered within the specified `width`, 
        padded with the specified `fillchar` (space by default).

        4. `count(substring)`: Returns the number of occurrences of a substring within the string.

        5. `encode(encoding='utf-8', errors='strict')`: Returns the encoded version of the string
         using the specified encoding.

        6. `endswith(suffix)`: Checks if the string ends with the specified suffix and returns
         `True` if it does, otherwise `False`.

        7. `expandtabs(tabsize=8)`: Expands tabs in a string to multiple spaces. By default, 
        each tab character is replaced by spaces up to the
         next tab stop.

        8. `find(substring)`: Returns the lowest index in the string where the substring is found,
         or -1 if it is not found.

        9. `format(*args, **kwargs)`: Formats the string using positional and keyword arguments.

        10. `format_map(mapping)`: Similar to `format()`, but takes a mapping object instead
         of separate arguments.

        11. `index(substring)`: Like `find()`, but raises an exception if the substring is not found.

        12. `isalnum()`: Returns `True` if all characters in the string are alphanumeric (letters or numbers),
         otherwise `False`.

        13. `isalpha()`: Returns `True` if all characters in the string are alphabetic (letters),
         otherwise `False`.

        14. `isdecimal()`: Returns `True` if all characters in the string are decimal characters,
         otherwise `False`.

        15. `isdigit()`: Returns `True` if all characters in the string are digits,
         otherwise `False`.

        16. `isidentifier()`: Returns `True` if the string is a valid identifier
         (e.g., variable name), otherwise `False`.

        17. `islower()`: Returns `True` if all characters in the string are lowercase,
         otherwise `False`.

        18. `isnumeric()`: Returns `True` if all characters in the string are numeric characters,
         otherwise `False`.

        19. `isprintable()`: Returns `True` if all characters in the string are printable,
         otherwise `False`.

        20. `isspace()`: Returns `True` if all characters in the string are whitespace characters,
         otherwise `False`.

        21. `istitle()`: Returns `True` if the string is in title case
         (i.e., each word starts with an uppercase character),
         otherwise `False`.

        22. `isupper()`: Returns `True` if all characters in the string are uppercase,
         otherwise `False`.

        23. `join(iterable)`: Joins the elements of an iterable (e.g., a list)
         into a single string using the string as a separator.

        24. `lower()`: Converts all characters in the string to lowercase.

        25. `maketrans(x, y, z)`: Returns a translation table to be used in `translate()`.

        26. `partition(separator)`: Splits the string at the first occurrence
         of the separator and returns 
        a tuple containing the part before the separator, the separator itself, 
        and the part after the separator.

        27. `replace(old, new, count)`: Replaces occurrences of a substring with another substring.

        28. `split(separator, maxsplit)`: Splits the string into a list of 
        substrings using the specified separator.

        29. `splitlines(keepends)`: Splits the string at line breaks 
        and returns a list of lines.

        30. `startswith(prefix)`: Checks if the string starts with 
        the specified prefix and returns `True` if it does, otherwise `False`.

        31. `strip(chars)`: Removes leading and trailing characters 
        (whitespace by default) from the string.

        32. `swapcase()`: Swaps the case of each character in the 
        string (lowercase becomes uppercase and vice versa).

        33. `title()`: Converts the string to title case
         (i.e., each word starts with an uppercase character).

        34. `translate(table)`: Returns a copy of the string 
        where each character has been mapped through the given translation table.

        35. `upper()`: Converts all characters in the string to uppercase.

        36. `zfill(width)`: Pads the string with zeros
         on the left until it reaches the specified width.


    ''')
def Lopts(l):
    l.append('five-new')
    print('l.append("five-new")\t:', "\033[31m" + str(l) + "\033[0m")
    l.count('one')
    print('l.count("one")\t\t:', "\033[31m" + str(l.count("one")) + "\033[0m")
    temp_list=l.copy()
    print('original - l\t\t:', "\033[32m" + str(l) + "\033[0m")
    print('temp_list\t\t:', "\033[34m" + str(l) + "\033[0m")
    print('l.index("two")\t\t:', "\033[31m" + str(l.index("two")) + "\033[0m")
    l.insert(3,"four")
    print('l.insert(3,"four")\t:', "\033[31m" + str(l) + "\033[0m")
    l.remove("nalu")
    print('l.remove("nalu")\t:', "\033[31m" + str(l) + "\033[0m")
    l.reverse()
    print('l.reverse()\t\t:', "\033[31m" + str(l) + "\033[0m")
    l.clear()
    print('l.clear()\t\t:', "\033[31m" + str(l) + "\033[0m")
    l.extend(['1','2','5','4','3'])
    print("l.extend([2','3','1'])  :", "\033[31m" + str(l) + "\033[0m")
    l.sort()
    print('l.sort()\t\t:', "\033[31m" + str(l) + "\033[0m")
    l.pop()
    print('l.pop()\t\t\t:', "\033[31m" + str(l) + "\033[0m")
def Ldefs():
    print(''' 
    This is from Chat gpt ,
     since i was not familiar with all these operations ,
     i used this as a refrence & also giving it here.
            Certainly! Here are shorter explanations for each list method:

    1. `append()`: Adds an element to the end of the list.

    2. `clear()`: Removes all elements from the list.

    3. `copy()`: Creates a shallow copy of the list.

    4. `count()`: Returns the number of occurrences of a specified
     element in the list.

    5. `extend()`: Adds the elements of another list to the end of
     the current list.

    6. `index()`: Returns the index of the first occurrence of a
     specified element in the list.

    7. `insert()`: Inserts a specified element at the specified
     position in the list.

    8. `pop()`: Removes and returns the last element of the list.

    9. `remove()`: Removes the first occurrence of a specified 
    element from the list.

    10. `reverse()`: Reverses the order of the elements in the list.

    11. `sort()`: Sorts the elements of the list in ascending order.
    ''')
def Topts(t):
   print('t.count(1)\t\t:', "\033[31m" + str(t.count(1)) + "\033[0m")
   print('t.count(1)\t\t:', "\033[31m" + str(t.index(3)) + "\033[0m")
def Tdefs():
    print('''
    This is from Chat gpt ,
     since i was not familiar with all these operations ,
     i used this as a refrence & also giving it here.

        `count()`: Returns the number of occurrences
         of a specified element within the tuple.

        `index()`: Returns the index of the first
         occurrence of a specified element within the tuple.
    ''')
def Dopts(d):
    temp_dict=d.copy()
    print('\t\t\t:temp_dict=d.copy()')
    print('original - d\t\t:', "\033[32m" + str(d) + "\033[0m")
    print('temp_dict\t\t:', "\033[34m" + str(temp_dict) + "\033[0m")
    print('d.values()\t\t:', "\033[31m" + str(d.values()) + "\033[0m")
    print('d.keys()\t\t:', "\033[31m" + str(d.keys()) + "\033[0m")
    keys=[1,2,3,4,5]
    values='hi'
    temp_dict=dict.fromkeys(keys,values)
    print('dict.fromkeys(Keys,values):', "\033[34m" + str(temp_dict) + "\033[0m")
    print("d.get('age')\t\t:", "\033[31m" + str(d.get('age')) + "\033[0m")
    print("d.items()\t\t:", "\033[31m" + str(d.items()) + "\033[0m")
    d.pop('namr')
    print("d.pop('namr')\t\t:", "\033[31m" + str(d) + "\033[0m")
    d.popitem()
    print("d.popitem()\t\t:", "\033[31m" + str(d) + "\033[0m")
    d.update({'hobby':'Sleeping'})
    print("d.update({'hobby':'Sleeping'})\t:", "\033[31m" + str(d) + "\033[0m")
    d.setdefault('name','Shanu')
    print("d.setdefault('name','Shanu')\t:", "\033[31m" + str(d) + "\033[0m")
    d.clear()
    print('d.clear() \t:', "\033[31m" + str(d) + "\033[0m","\033[32m" + 'empty' + "\033[0m\n\n\n")
def Ddefs():
    print('''   
    Certainly! Here's a brief explanation of each dictionary operation:

    1. `clear()`: Removes all items from the dictionary.

    2. `copy()`: Creates a shallow copy of the dictionary.

    3. `fromkeys()`: Creates a new dictionary with keys from 
        a specified iterable and values set to a specified value.

    4. `get()`: Returns the value associated with a specified
     key, or a default value if the key is not found.

    5. `items()`: Returns a view object that displays a list of
     dictionary's (key, value) tuple pairs.

    6. `keys()`: Returns a view object that displays a list of
    all the keys in the dictionary.

    7. `values()`: Returns a view object that displays a list of
     all the values in the dictionary.

    8. `pop()`: Removes and returns the value associated with
     a specified key.

    9. `popitem()`: Removes and returns an arbitrary (key, value)
    pair from the dictionary.

        10. `setdefault()`: Returns the value of a specified key,
     and if the key does not exist, inserts the key with a specified value.

    11. `update()`: Updates the dictionary with the key-value
     pairs from another dictionary or iterable.

    ''')
def pyoperators():
    print('''
    In py we Have -
        1. Arithmetic operators
        2. Assignment operators
        3. Comparison operators
        4. Logical operators
        5. Identity operators
        6. Membership operators
        7. Bitwise operators

    Enter corresponding number to continue   \n    Press \033[31m x\033[0m to skip \t\t
        ''')
    choice=''
    while True:
        opt = input('-')
        if opt == 'x':
            return
        try:
            choice=int(opt)
            if(choice>7 or choice<1):
                raise ValueError("invalid")
            if(choice>0 and choice<8):
                break
        except ValueError:
            print("Invalid Input ,Please try again...")
        except:
            print("Invalid Input ,Please try again...")
    if(choice==1):
        print(''' 
        - Addition        : +
        - Subtraction     : -
        - Multiplication  : *
        - Division        : /
        - Floor division  : //
        - Modulus         : %
        - Exponentiation  : **
        ''')
    elif(choice==2):
                print(''' 
        - Assignment                     : =
        - Addition assignment            : +=
        - Subtraction assignment         : -=
        - Multiplication assignment      : *=
        - Division assignment            : /=
        - Floor division assignment      : //=
        - Modulus assignment             : %=
        - Exponentiation assignment      : **=
        - Bitwise AND assignment         : &=
        - Bitwise OR assignment          : |=
        - Bitwise XOR assignment         : ^=
        - Bitwise left shift assignment  : <<=
        - Bitwise right shift assignment : >>=
        ''')
    elif(choice==3):
        print('''
        - Equal to                       : ==
        - Not equal to                   : !=
        - Greater than                   : >
        - Less than                      : <
        - Greater than or equal to       : >=
        - Less than or equal to          : <=
          \033[36mfor eg : f"{10}=={10}"  \033[0m
        
        '''
        )
    elif(choice==4):
        print('''
        - Logical AND                    : and
        - Logical OR                     : or
        - Logical NOT                    : not
         \033[36mfor eg expression = "2 > 10 and 4 > 10"  \033[0m
        
        ''')
    elif(choice==5):
        print('''
        - Identity                       : is
        - Non-identity                   : is not
        ''')
    elif(choice==6):
        print('''
        - Membership                     : in
        - Not membership                 : not in

        \033[36mfor eg :  f"{t} in my_str"  \033[0m
        ''')
    elif(choice==7):
        print('''
        - Bitwise AND                    : &
        - Bitwise OR                     : |
        - Bitwise XOR                    : ^
        - Bitwise NOT                    : ~
        - Bitwise left shift             : <<
        - Bitwise right shift            : >>
         \033[36mfor eg : f"{'one'} in l & temp_list"  \033[0m
        
        ''')
    while True:
        formula=input("Carefully enter the Formula [eg :\033[35m9+9\033[0m  ]\n    Press \033[31m x\033[0m to skip\n  & No spaces    :  ")
        try:
            # print(eval(formula))
            print(f'The Result For the Formula ({formula}) is \033[32m:{eval(formula)} \033[0m')
            break 
        except:
            print("Invalid formula ,Please try agian...\n\n")
def nationality():
    name=input('Enter your name :')
    c=['india','usa','france','spain','uae']
    cntry=input(''' 
    Which amoung these countries do you belong:
    1)\033[32mIndia\033[0m
    2) USA
    3) France
    4) Spain
    5) UAE
    ''').lower()
    
    if(cntry in c):
        if(cntry=='india'):
            print(f'भारत({cntry.upper()}) से आपका स्वागत है, श्री.{name.title()}"')
        elif(cntry=='usa'):
            print(f'Welcome Mr.{name.title()}" from ({cntry.upper()})')
        elif(cntry=='france'):
            print(f'Bienvenue M.{name.title()}" de {cntry.upper()}')
        elif(cntry=='spain'):
            print(f'Bienvenido Sr.{name.title()}" de la {cntry.upper()}')
        elif(cntry=='spain'):
            print(f'Bienvenido Sr.{name.title()}" de la {cntry.upper()}')
        elif(cntry=='uae'):
            print(f'مرحباً بك يا السيد {name.title()} من الإمارات العربية المتحدة ({cntry.upper()})')
    else:
         print(f'Actually Mr.{name.title()} , Citizens of {cntry.capitalize()} are not welcome😏')        
my_str ='this is  my string'
print('1.The string we are using\t\t:'+"\033[96m" + my_str + "\033[0m")
choice=input('''wanna see all operations that can be performed on this String...
Enter \033[31m s \033[0m
Enter \033[31m d \033[0mdescription
Press \033[31m ↵\033[0m to skip    :''') 
if(choice=='s'):
    Sopts()
elif(choice=='d'):
    Sdefs()
else:
    print('\033[2J')
# list
l=['one','two','three','nalu']
print('2.The List  we are using\t\t:'+"\033[96m" + str(l) + "\033[0m")
choice=input('''wanna see all operations that can be performed on this List...
Enter \033[31m s \033[0m
Enter \033[31m d \033[0mdescription
Press \033[31m ↵\033[0m to skip    :''') 
if(choice=='s'):
    Lopts(l)
elif(choice=='d'):
    Ldefs()
else:
    print('\033[2J')
# tuple
t=(1,1,1,2,3,4,5,6,7,8,9)
print('3.The Tupplw  we are using\t\t:'+"\033[96m" + str(t) + "\033[0m")
choice=input('''wanna see all operations that can be performed on this tupple...
Enter \033[31m s \033[0m
Enter \033[31m d \033[0mdescription
Press \033[31m ↵\033[0m to skip    :''') 
if(choice=='s'):
    Topts(t)
elif(choice=='d'):
    Tdefs()
else:
    print('\033[2J')
# dictinary section
d={'namr':'shanu','age':2,'place':'allepy'}
print('4.The Dictinary  we are using\t\t:'+"\033[96m" + str(d) + "\033[0m")
choice=input('''wanna see all operations that can be performed on this ...
Enter \033[31m s \033[0m
Enter \033[31m d \033[0mdescription
Press \033[31m ↵\033[0m to skip    :''') 
if(choice=='s'):
    Dopts(d)
elif(choice=='d'):
    Ddefs()
else:
    print('\033[2J')
print('5.Operators in Python')
pyoperators()
print('6.Natinality')
nationality()
print('\n\n7.Display the first 10 natural numbers using while loop.')
i=1
while(i<=10):
    print(i)
    i=i+1
print('8.reverse the list using loop.')
lis=['one','two','three','four','five','six','seven']
tmp=[]
for i in lis:
    tmp.insert(0, i)
print(tmp)
print('9. Reverse the digits of integer.')
while(True):
    try:
        n=list(input("enter -"))
        n=n[::-1]
        print(int(''.join(n)))
        break
    except:
        print("Invalid Entry ,try again ")
print('Patern No : 10')
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print('Patern No : 11')
for i in range(1, 6):
    print("* " * i)
for i in range(4, 0, -1):
    print("* " * i)



