import statistics 

class Student: 
    
    # To access class variables need to use the instance .self  or the class  itself .Student
    
    email_prefix = ['@uel.ac.uk', '@uel.admin.uk']  
    
    # Init method for a class 
    
    def __init__(self, first, last, grades):
        self.first = first
        self.last = last 
        self.grades = grades 
        self.email = f'{first}{last}{self.email_prefix[1]} '    
        self.average = f' Average Grade for {first} {last} {sum(grades) // len(grades)}%'
         
    full_name = lambda self : f'{self.first} {self.last}'
        
        
        
        
student_1 = Student('Joe','Jacques', [145, 66, 77,88])

# Calling a call method full_name()



print(Student.full_name(student_1))
print(student_1.email)
print(student_1.average)