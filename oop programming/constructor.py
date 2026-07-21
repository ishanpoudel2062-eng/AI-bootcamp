class employee:
    def __init__(self,name,salary,passion):
         self.name=name
         self.salary=salary
          
         print("employee is created\n")
        
    def getdetails(self):
        print(f"the name of the worker is {self.name}")
        print(f"the salary of the worker is {self.salary}")
      
       
abhiyan=employee("ishan",400000,)
abhiyan.getdetails()
