  #this program indicates DICTIONARIES 
  # it also storing of values we can store different data types

student={"name":"SAJEED","USN":"2BL20IS031","ROLL ON":20,"BRANCH":"INFORMATION SCIENCE ENGINEERING"}
print(student)                            #unordered dictionaries
print(student["USN"])                     #ordered dictionaries
print(len(student))


x=student.get("BRANCH")                      # using get function we can access 
print(x)

x=student.keys()                                        # how to know the keys   using key function 
print(x)
student["age"]=34
print(x)
y=student.values()                                                          #how to know the values  using value function
print(y)

z=student.items()                                                 #how to know the both values and keys using item function 
print(z)


parent={
    "child_1":{
        "name":"child",
        "age":10,
 },
 "child_2":{
    "name":"anotherchild",
    "age":8
 }
}
print(parent)
r=parent.get("child_1")
print(r)

food={"breakfast":"dosa","lunch":"mutton briyani","dinner":"paneer tika"}
b={"breakfast","lunch","dinner"}
h=food.fromkeys(b)
print(h)
p=food.get("lunch")
print(p)
food.setdefault("breakfast","idli and vada")               #setdefalut is used for not changing value in dictionaries for making fixed till the end 
print(food)
 