#this program indicates the AREA OF RECTANGLE,SQUARE,CIRCLE
#lets start with the functions,class and objects
from re import A


class Area:
    def __init__(self,name,age,branch,semester):               #CONSTRUCTOR
        self.name=name
        self.age=age
        self.branch=branch
        self.semester=semester 


    def display(self):                                 #METHOD
        print("the name  is ->",self.name)
        print("the age is->",self.age)
        print("the branch is->",self.branch)
        print("the semester is->",self.semester)
sc=Area("sajeed",22,"information science",5)
sc.display()