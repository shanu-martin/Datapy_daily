import urllib.request
import importlib.util
import os
import shutil
import sys

script_directory = os.path.dirname(__file__)
demo_directory = os.path.join(script_directory, 'demo')
sys.path.append(demo_directory)
current_directory = os.getcwd()
new_directory = 'demo'
new_directory_path = os.path.join(current_directory, new_directory)
os.makedirs(new_directory_path, exist_ok=True)

# Download from my git
url = 'https://raw.githubusercontent.com/shanu-martin/Datapy_daily/main/user_module.py'
response = urllib.request.urlopen(url)
user_module_code = response.read()
file_path = os.path.join(new_directory_path, 'user_module.py')
with open(file_path, 'wb') as file:
    file.write(user_module_code)
spec = importlib.util.spec_from_file_location('user_module', file_path)
user_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(user_module)


source_directory = os.path.dirname(__file__)
demo_directory = os.path.join(source_directory, 'demo')

sys.path.append(demo_directory)

from user_module import fact as fact, check_prime as primer, fibonacci as fib, arm as arm, nsum as nsum
 
#                                                     Question 1
def userfns():
    command = input('Do you want to use its Functionalities? \033[94m[y]\033[0m or \033[91m[n]\033[0m: ').lower()
    if command =='y':
        fact(input('Factorial :'))
        primer(input('Check Prime :'))
        fib(input('Limit for Fibonacci Series  :'))
        arm(input('Check Armstrong  :'))
        nsum(3,4,5,6,7,8,9)
    else:
        print(f'User Module : \033[91m Disconnected \033[0m')
        return
userfns()
#                                                     Question 2
print(f'Folder Name : \033[32m demo \033[0m')
print(f'\033[94m\t\tQuestion 2\n\033[0m')
Q2name=input('File Name :')
if Q2name=='':
    Q2name='sample'
Q2name+='.txt'
pathQ2=os.path.join(new_directory_path, Q2name)
with open(pathQ2,'w+') as q2:
    q2.write('''Hi ...
    Good Morning.
    Welcome to Python.''')
    q2.seek(0)
    con=q2.read()
    print(f'\033[32m \t\t\t{Q2name}\033[0m')
    print(f'\033[94m{con}\033[0m')
#                                                     Question 3
print(f'Files inside : \033[32m demo \033[0m')
def list_files(directory):
    files = []

    def list_files_recursively(directory):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                if item=='user_module.cpython-312.pyc':
                    continue
                files.append(item)
                print(f'\t\t\t\t\033[96m{item}\033[0m')
            elif os.path.isdir(item_path):
                list_files_recursively(item_path)
    
    list_files_recursively(directory)
    
    return files
files = list_files(demo_directory)

modes = {
    'r': '\033[94mRead Only\033[0m \n\t\t[Opens file for reading. Raises FileNotFoundError if file does not exist.]',
    'r+': '\033[94mRead & Write\033[0m \n\t\t[Opens file for both reading and writing. Raises FileNotFoundError if file does not exist.]',
    'w': '\033[94mWrite Only\033[0m \n\t\t[Creates new file if exists overwrite it!]',
    'w+': '\033[94mBoth write & read\033[0m\n',
    'a': '\033[94mAppend\033[0m \n\t\t[Creates new file if doesnt exist & appends. Never overwrites!]',
    'a+': '\033[94mAppends & Read\033[0m\n',
    'b': '\033[94mBinary mode\033[0m \n\t\t[try creating a \033[91m.py file with "wb"\033[0m]',
    't': '\033[94mText mode\033[0m \n\t\t[Opens file in text mode]',
    'x': '\033[94mExclusive creation\033[0m \n\t\tn[Creates a new file. Raises FileExistsError if the file already exists.]'
}
def mprint():
    for key, value in modes.items():
        print(key, ":", value)

def q3(path):
    try:
        command = input('Do you want to continue to Q3? \033[91m[⏎ ]\033[0m to contiue\n \t\t\t\t\033[91m[x]\033[0m to exit : ').lower()
        if command=='x':
            raise Exception("Exiting...")
        else:
            pass
        mprint()
        mode = input('Enter the file mode [\033[91mLeave empty for default (w+)\033[0m]: ')
        filename = input('Enter the file name [\033[91mLeave empty for default (sample.txt)\033[0m]: ')
        
        if mode == '':
            mode = 'w+'
        if filename == '':
            filename = 'sample.txt'
        
        extn = '.py' if 'b' in mode else '.txt'
        filename += extn
        file_path = os.path.join(path, filename)
        
        print(f'\t\t\t\ttrying to create\033[32m {filename}...\033[0m')
        
        with open(file_path, mode) as f:
            if 'w' in mode or 'a' in mode:
                f.write('Chumma kurach text')
            if 'r' in mode or '+' in mode:
                f.seek(0)
                content = f.read()
                print("File content:", content)
            if 'py' in extn:
                f.write("print('Goodbye, world!')")
                
        print('\n\n\033[32mFile operation completed successfully!\033[0m')
    except Exception as e:
        print(f'\033[91mError: {e}\033[0m')
q3(demo_directory)


# footer
# footer of first question
print('''\n\nAs you may have noticed,
this program execution  created a file which has code of user_module.py from my personal git repo''')
try:
    command = input('Do you want to keep it? \033[94m[y]\033[0m or \033[91m[n]\033[0m: ').lower()
    if(command == 'y'):
        print("\033[32mFile saved\033[0m")  
    elif(command == 'n'):
        shutil.rmtree(new_directory_path)
    else:
        raise ValueError("Invalid entry")
except Exception as e:
    print(f"\033[91mError: {e}\033[0m")
    os.remove('ztemp_shanu.py')
    print("\033[91mFile removed automatically!\033[0m")
