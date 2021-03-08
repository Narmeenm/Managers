from employee import *
from room import *
from team import *

#Inserting random data to different types of class
teams = [Team(1,"BlockChain",5),Team(2,"RPI",4)]
employees =[Empolyee("Kimi","Kingsiton","0509606101","developer",teams[0].id),Empolyee("Kuda","Kwashai","050956722","software-engineer",teams[0].id),Empolyee("Samy","heny","050954022","CFO",teams[1].id)]
managers = [Manager("Ramy","Mask","+4468775678","software team leader",teams[1].id),Manager("Karim","Onsa","+346629345","HR team leader",teams[1].id)]
rooms = [Room(1,2),Room(2,4)]

teams[0].add_employee(employees[0])
teams[0].add_employee(employees[1])
teams[0].add_employee(managers[0])
teams[1].add_employee(managers[1])

rooms[0].add_employee(employees[0])
rooms[0].add_employee(employees[1])
rooms[0].add_employee(employees[2])
rooms[1].add_employee(managers[1])

#printing employees per team
for team in teams:
    print("These are employees of",team.teamName,"team")
    team.show_all_employee_in()

print("***************")
#removing specific employee in a team
teams[0].remove_employee(employees[0])



# the manager update the status of the employee
managers[0].update_employees_status(employees[0])
print(employees[0].get_fullName)

# removing unemployee from the teams and the rooms
for room in rooms:
    if room.is_employee_in(employees[0]):
        room.remove_employee(employees[0])

for team in teams:
    if team.is_employee_in(employees[0]):
        team.remove_employee(employees[0])


print("***************")
# to check if I removed correct the unemployee from the room
print(rooms[1].is_employee_in(employees[0]))

#printing all the employee in the company
Empolyee.print_all_employees(employees)

print("****************")
#printing employees per room
for room in rooms:
    print("These are employees in room number",room.roomNum)
    room.show_all_employee_in()
print("****************")

#removing specific employee in a room
rooms[0].remove_employee(employees[1])

# how to find specific employee between all the teams by searching in list instance of the employees
for team in teams:
    if team.is_employee_in(employees[1]):
        print(team.teamName)

# I thought about different solution for finding the team of specific
# by adding id instance in Team class and passing it to the Employee class, in this way I changed the o(n) from : o(n*m) in the previous solution, and know is o(n)
for team in teams:
    if employees[2].team_id == team.id:
        print(team.teamName)
print("*************")
# printing the manager name per team
for team in teams:
    print(team.teamName,"manager is",team.find_team_manager())

print("**** all the employees' emails ****")
#printing all employee emails, with using property decorator:
for employee in employees:
    print(employee.email)
