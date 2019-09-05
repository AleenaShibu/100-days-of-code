class College:
    def __init__(self,name,department):
        self.name = name
        self.department = department
    def print_details(self):
        print(f"{self.name},{self.department}")
class Student(college):
    def __init__(self,name,department,roll_no):
        college.__init__(self,name,department)
        self.rollno = roll_no
    def prinit_details(self):
        college.print_details(self)
        print(f"{self.roll_no}")

p = student("Shalini","Chemistry",3)
p.print_details()
class Teacher(college):
    def __init__(self,name,deparment,college_id):
        college.__init__(self,name,department)
        self.college_id = college_id

    def print_details(self):
        college.print_details(self)
        print(f"{self,college_id}")

p1 = teacher("Diviya","Chemistry",2013)
p1.print_detail()
