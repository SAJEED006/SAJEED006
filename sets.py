# THIS PROGRAM INDICATES SETS IN PYTHON 

movies={"ek tha tiger","race 3","sulthan","drishayam","raees"}             #sets
print(movies) 
for x in movies:                                           #printing single value in string 
    print(x)
print("race 3" in movies)
print("sanam teri kasam" in movies)                                        #present or not 
movies.add("dilwale")
print(movies)
newmovies={"tarzan the wonder car","golmaal"}                                     # updating the sets using update function
movies.update(newmovies)
print(movies)
movies.remove("golmaal")                       #removing the value in the sets 
print(movies)
movies.discard("race 3")
print(movies)
movies.pop()                           #removing the last value in sets
print(movies)
movies.clear()                                        #removing all the values in sets using the clear function.
print(movies)