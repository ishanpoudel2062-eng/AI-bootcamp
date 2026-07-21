class person:
    def intro1(self):
     self.a=input("enter the name: ")
     
    
class student(person):
        def intro2(self):
            self.n=int(input("enter the class: "))
           
            
class college(student):
     def intro3(self):
            c=int(input("enter the clg name: "))
            print(f"Name is: {self.a}")
            print(f"Name is: {self.n}")
            print(f"class is: {c}")
               
            
s=college()
s.intro1()
s.intro2()  
s.intro3()          