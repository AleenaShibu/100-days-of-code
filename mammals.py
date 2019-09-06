class Mammals:
    def __init__(self,name,type,):
          self.name = name
          self.type = type
    def print_category(self):
          print(f"{self.name}{self.type}")
class Human(Mammals):
    def __init__(self,name,type,age):
          Mammals.__init__(self,name,type)
          self.age = age
    def print_category(self):
          Mammals. print_category(self)
          print(f"{self.age}")
p = Human("Ravi","Terresrrial",23)
p.print_category

class Dolphin(Mammals): 
    def __init__(self,name,type,age):
          Mammals.__init__(self,name,type)
          self.age = age
    def print_category(self)
          Mammals.print_category(self)
          print(f"{self.age}") 
p1 = Human("Pacific bottlenose dolphin","Aquatic",20)
p1.print_category()

