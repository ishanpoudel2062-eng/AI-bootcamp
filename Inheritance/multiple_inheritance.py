class father:
    def intro1(self):
        self.name1=input("enter father name: ")
        self.occu1=input("enter father occupation: ")
        
class mother:
     def intro2(self):
        self.name2=input("enter mother name: ")
        self.occu2=input("enter mother occupation: ")
        
class child(father,mother):       
 def intro3(self):
        self.name3=input("enter son name: ")
        print(f"Name of father: {self.name1}\n Father occupation: {self.occu1}")
        print(f"Name of Mother: {self.name2}\n Mother occupation: {self.occu2}")
        print(f"Name of son: {self.name3}")
        
c=child()
c.intro1()
c.intro2()
c.intro3()        
                   