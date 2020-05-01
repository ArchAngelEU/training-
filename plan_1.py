movies = []



def add_movie():
    movie = input('Hello What is the Name of the movie which you want to add?')
    movies.append(movie)
    return movies
    
def list_movies():
        print(movies)


try:

    options = [1,2,3,4,'Q', 'q']
    decison = int(input(f'''Please Select an Option: \n
    1: Add Movie To List 
    2. List Movies 
    3. 
    4. Type Q to Quit \n 
    :'''))
    
    if decison == 1:
        add_movie()
    elif decison == 2:
        list_movies()
    elif decison == 4:
        exit()  
except:
    
    print (f'Invalid Input, must be one of the options {options} ')
    exit()
    
