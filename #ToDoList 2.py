#ToDoList 2

#Natalia

MoviesWatched= ["Lion King","Tangled", "Toy Story", "Forest Gump", "Barbie", "Us"]
#Allows you to edit and view Movie Watch list by adding, removing, and marking movies as watched
def ToDoList():
    print ("Welcome to the Your Movie Watch list")
    print("Please chose an action: (Type in an number between 1-5)")
    print("1. Add Movie\n2. View List \n3. Mark movie as watched \n4. Remove Movie \n5. Remove all Movies \n6. Sort Alphabetically \n7. Print the number of Movies in list \n8.Quit")
    option=int(input("Option: "))

    if (option==1): 
        x=input("Movie Name:")
        MoviesWatched.append(x)
        print(MoviesWatched)
        ToDoList()
    if(option==2):
       print(MoviesWatched)
       ToDoList()
    if (option==3): 
        ans=input("What Movie From Your LIst Did You Watch?")
        i=MoviesWatched.index(ans)
        MoviesWatched[i]=ans+"X"
        print(MoviesWatched)
        ToDoList()
    if (option==4):
        z=input("What Movie Would you like to remove from your List?")
        MoviesWatched.remove(z)
        print(MoviesWatched)
        ToDoList()
    if(option==5):
        MoviesWatched.clear()
        print(MoviesWatched)
        ToDoList()
    if(option==6): 
        MoviesWatched.sort
        print(MoviesWatched)
        ToDoList()
    if(option==7): 
        size=len(MoviesWatched)
        print(size)
        ToDoList()
    if(option==8):
        print("Goodbye!") 
        quit()

ToDoList()