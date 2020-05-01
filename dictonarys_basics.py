import statistics


student = {
    'name': 'Joe', 
    'grades': [98,60,44,72,15]   
}

def average_grade(students):
    for key, value in students.items():
        if key == 'grades':
            return (f' Average Grade: {statistics.mean(students[key])}')
        
        
print(average_grade( {'grades': [23,44,55,66,77,777]})) 
            
        
    
    
    