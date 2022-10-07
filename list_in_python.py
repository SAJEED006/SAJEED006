


fruits=["banana","apple","mango","orange"]              # using list, in this we will create a list
print(fruits)
fruits[2]="grapes"
print(fruits)
another_fruits=["kiwi","pineapple"]                     #change the variables with another frutis names
fruits[1:2]=another_fruits
print(fruits)

list_1=["sajeed","maaz","adil"]
list_2=["azeem","mudasar","avinash","vinit"]
print(list_1+list_2)                                      #adding the 2 given list in python into single list
list_3=list_1+list_2
another_fruits[0:1]="pompgranrte","pomogrante","pomogrante"  #replacing the list  with one particular fruit
print(another_fruits)
list_1.insert(1,"sajeed")                                          #insert function 
print(list_1)                       
list_2.append("maaz")
print(list_2)                                               #append functon directly works no index and ranging 
fruits.extend(another_fruits)                              #adding two lists using extend functon
print(fruits)
list_1.remove("maaz")
print(list_1) 
list_6=["java","c++","python","c"]                                           # Deleteing the value in the list
list_6.pop(1)
print(list_6)                                                   #deleting for particular index 
del list_6[1]
print(list_6)
