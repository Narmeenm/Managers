class Room():
   def __init__(self, roomNum, capacity):
        self.roomNum = int(roomNum)
        self.capacity = int(capacity)
        self.reserved = False
        self.employees = []

   def check_capacity(self):
        if len(self.employees) >= self.capacity:
            self.reserved = True # this mean the room full
            return False
        return True

   def add_employee(self,employee):
       if employee.getStatus():
           if self.check_capacity():
              self.employees.append(employee)
              return True
           return "this room is full,Please reserve different room"
       print(employee.firstName, "is unemployee, he could not enter the room")

   def remove_employee(self,employee):
           if self.is_employee_in(employee):
               self.employees.remove(employee)

   def show_all_employee_in(self):
      for self.employee in self.employees:
          print(self.employee.get_fullName)

   def is_employee_in(self,employee):
       for self.employee in self.employees:
           if self.employee == employee:
               return True
           return False
