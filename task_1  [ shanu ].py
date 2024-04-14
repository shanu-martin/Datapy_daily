bnr = '''
########    ###     ######  ##    ##            ##   
   ##      ## ##   ##    ## ##   ##           ####   
   ##     ##   ##  ##       ##  ##              ##   
   ##    ##     ##  ######  #####      ####     ##   
   ##    #########       ## ##  ##              ##   
   ##    ##     ## ##    ## ##   ##             ##   
   ##    ##     ##  ######  ##    ##          ###### 
'''
print("\033[96m" + bnr + "\033[0m")     #ASCII ART 
temp_list = []


def nsum():
    print('''Enter numbers to be added one by one & when finished simply type x
                Float -No Problem
                Many Inputs -I dont Mind😛
                Invalid Inputs -Still No Problem 
                            try it .....''')
    while True:
        temp = input('-')
        if temp == 'x':
            break
        try:
            temp_list.append(float(temp))
        except:
            print("Invalid Input ,Please Continue...")
    print("Total:", sum(temp_list))


print('Hello _ world')
print("""--------------------------------------------------------------""")
# 2.Python program to do sum of 'n' numbers, after taking inputs from the user
nsum()
print("""--------------------------------------------------------------""")


# 3. Write a python program to find the area of a square and rectangle.
def nArea(x, y=''):
    
    if (y == ''):
        y = x
    else:
        y=int(y)
    print('Area :', x * y)

print('''To get Area of Rectangle Enter Both Length & Breath,if its a Square Enter Any side : ''')
length=int(input("Length [One side if it's a square] :"))
breath=input("Enter Breath if it's a Rectangle only:")
nArea(length, breath)  
print("""--------------------------------------------------------------""")
# 4. Create a string & get the characters of string from 2 to 18 using both positive and negative indexing.
Mstr = 'Create a string & get the characters'
print("Original String :"+"\033[31m" + Mstr + "\033[0m")
print("\033[96m" + 'My_String[2:18]      =>' + "\033[0m" +Mstr[2:18])
# print(len(Mstr))
print("\033[96m" + 'My_String[-34:-18] =>' + "\033[0m" +Mstr[-34:-18])
print("""--------------------------------------------------------------""")
# 5. Create and print a list with same and different items.
My_lst = [1, 1, 2, 2, 3, 4, 5]
print("\033[96m" + 'Original List =>' + "\033[0m" ,My_lst)
# 6. Access an item from the list using its index.
print("\033[96m" + 'My_lst[4] =>' + "\033[0m" ,My_lst[4])
# 7. Access an item from the list using negative index.
print("\033[96m" + 'My_lst[-2] =>' + "\033[0m" ,My_lst[-2])

# 8. Modify an item in the list.
My_lst[1] = "Modified"
print(My_lst)
# 9. Access the items in the list using slicing.
new = My_lst[1:3]
print(new)
print("""--------------------------------------------------------------""")
# 10. Create a dictionary and print it.
hai = {
    1: 'h',
    2: 'a,',
    3: 'i'
}
print(hai)
# 11. Change the value of a key.
hai[1] = 'd'

print(hai)
