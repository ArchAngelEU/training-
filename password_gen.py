import string 
from random import *

try:
    
    def password_gen(start, end):
        
        """  A lightweight module that will generate a random password. 
            required Params: length_start(int), length_end(int)
        """
        
        letters = (f'{string.ascii_letters}{string.punctuation}{string.digits}')
        password =  "".join(choice(letters) for x in range(randint(start,end)))
        return print(f' Password is: {password}')   
    
except (TypeError, ValueError):
    print ('Invalid input: Make sure the following: \n 1. You have two inputs, \n 2. They are both ints, \n 3. First value is larger or the same as the second')


