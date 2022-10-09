animals=("cat","goat","camel","cow","sheep")                              # this program indicates tuples   ``
print(type(animals))                                   #tuple is different from list,tuple use  different data types.
print(animals[2])   
print(animals) 
print(animals)


#there are 4 different data types namely 1.list,2.tuples,3.order,4.dictionary
#range of indexes and negative indexing
languages_in_computer=("c++","java","python","c","javascript","pascal","Basic","html and css","Sql","c++","c++") 
print(languages_in_computer)
print(languages_in_computer[-1])     #negative indexing 
print(languages_in_computer[0:5])
print(languages_in_computer[:0])            # behind zero there is nothing since zero is starting index 
print(languages_in_computer[0:])        #printing all values in  output 
print(languages_in_computer.count("javascript"))
print(languages_in_computer.count("c++"))           #counting values 
print(languages_in_computer.index("html and css"))
print(languages_in_computer.index("c++"))             #checking value of index using value name 
print(len(languages_in_computer))              #finding total values in tuples  using len function 