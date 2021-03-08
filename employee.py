class Empolyee():
   def __init__(self, firstName,lastName, phoneNum,positionName,team_id):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNum = phoneNum
        self.__status = True # employee = True / unemployee =False
        self.positionName = positionName
        self.team_id = team_id

   def getStatus(self):
       return self.__status

   def setStatus(self,status):
       self.__status = status

   @property
   def get_fullName(self):
       return'{} {}'.format(self.firstName, self.lastName)

   @get_fullName.setter
   def get_fullName(self,name):
       first, last = name.split(' ')
       self.firstName = first
       self.lastName = last

   @property
   def email(self):
       return'{}.{}@gmail.com'.format(self.firstName, self.lastName)

   def print_all_employees(employees):
       for employee in employees:
           if (employee.getStatus()):
            print(employee.firstName ,employee.phoneNum ,employee.positionName)


class Manager(Empolyee):
    def __init__(self, firstName,lastName, phoneNum,positionName,team_id):
        self.isManager = True
        super().__init__(firstName,lastName, phoneNum,positionName,team_id)

# only the Manager can change employee's status
    def update_employees_status(self,employee):
       employee.setStatus(False)
       print(self.get_fullName,"changed employee status")
