from room import *
# The reason that I did Team class inherit from the Room class is to avoid repetition of two methods:
#                 def remove_employee(self,employee)
#                 def show_all_employee_in(self)
#                 def is_employee_in(self,employee):
class Team(Room):
   def __init__(self, id,teamName, teamCapacity):
        self.teamName = teamName
        self.teamCapacity = int(teamCapacity)
        self.employees =[]
        self.id = int(id)

   def check_capacity(self):
        if len(self.employees) < self.teamCapacity:
            return True
        return False

   def add_employee(self,employee):
       if employee.getStatus():
          if self.check_capacity():
             self.employees.append(employee)
             return True
          print("this team is full")
       print(employee.firstName, "is unemployee you could not enter the team")

   def find_team_manager(self):
       for self.employee in self.employees:
           if self.employee.__class__.__name__ == 'Manager':
               return self.employee.get_fullName
