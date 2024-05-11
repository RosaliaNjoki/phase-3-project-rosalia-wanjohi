from models.students import Student
from models.hostels import Hostel
from models.rooms import Room
from models.allocations import Allocation

def exit_program():
    print("Goodbye!")
    exit()

# implementing student function 

def list_students():
    students = Student.get_all()
    for student in students: 
        print(student)


def find_student_by_id():
    id_ = input("Enter the student's id: ")
    student = Student.find_by_id(id_)
    print(student) if student else print (f'Student {id_} not found')


def create_student():
    name = input("Enter the student's name: ")
    gender = input("Enter the student's gender: ")
    department = input("Enter the student's department: ")
    try: 
        student = Student.create(name, gender, department)
        print(f'Success: {student}')
    except Exception as exc: 
        print("Error creating student: ", exc)


def update_student():
    id_ = input("Enter the student's id: ")
    if student := Student.find_by_id(id_):
        try:
            name = input("Enter the student's new name: ")
            gender = input("Enter the student's new gender: ")
            department = input("Enter the student's new department: ")

            student.name = name
            student.gender = gender
            student.department = department

            student.update()
            print(f'Success: {student}')
        except Exception as exc:
            print("Error updating student: ", exc)
    else:
        print(f'Student {id_} not found')


def delete_student():
    id_ = input("Enter the student's id: ")
    if student := Student.find_by_id(id_):
        student.delete()
        print(f'Student {id_} deleted')
    else:
        print(f'Student {id_} not found')
    
# Implementing hostel fuction 

def list_hostels():
    hostels = Hostel.get_all()
    for hostel in hostels: 
        print(hostel)


def find_hostel_by_id():
    id_ = input("Enter the hostel's id: ")
    hostel = Hostel.find_by_id(id_)
    print(hostel) if hostel else print (f'Hostel {id_} not found')


def create_hostel():
    name = input("Enter the hostel's name: ")
    capacity = int(input("Enter the hostel's capacity: "))  # Convert input to integer
    try: 
        hostel = Hostel.create(name, capacity)
        print(f'Success: {hostel}')
    except Exception as exc: 
        print("Error creating hostel: ", exc)


def update_hostel():
    id_ = input("Enter the hostel's id: ")
    if hostel := Hostel.find_by_id(id_):
        try:
            name = input("Enter the hostel's new name: ")
            capacity = int(input("Enter the hostel's new capacity: "))  # Convert input to integer
            hostel.name = name
            hostel.capacity = capacity

            hostel.update()
            print(f'Success: {hostel}')
        except Exception as exc:
            print("Error updating hostel: ", exc)
    else:
        print(f'Hostel {id_} not found')


def delete_hostel():
    id_ = input("Enter the hostel's id: ")
    if hostel := Hostel.find_by_id(id_):
        hostel.delete()
        print(f'Hostel {id_} deleted')
    else:
        print(f'Hostel {id_} not found')

#Implementing room function 
 
def list_rooms():
    rooms = Room.get_all()
    for room in rooms: 
        print(room)
    

def find_room_by_id():
    id_ = input("Enter the room's id: ")
    room = Room.find_by_id(id_)
    print(room) if room else print (f'Room {id_} not found')

def create_room():
    room_number = input ("Enter the room's room_number: ")
    capacity = input("Enter the room's capacity: ")
    hostel_id = input("Enter the room's hostel-id: ")
    try: 
        room = Room.create(room_number, capacity, hostel_id)
        print(f'Success: {room}')
    except Exception as exc: 
        print("Error creating room: ", exc)

def update_room():
    id_ = input("Enter the room's id: ")
    if room := Room.find_by_id(id_):
        try:
            room_number = input("Enter the rooom's new room_number: ")
            room.room_number= room_number
            capacity = input("Enter the room's new capacity: ")
            room.capacity=capacity
            hostel_id = input("Enter the room's new hostel_id: ")
            room.hostel_id = hostel_id

            room.update()
            print(f'Success: {room}')
        except Exception as exc:
            print("Error updating room: ", exc)
    else:
        print(f'Room {id_} not found')


def delete_room():
    id_ = input("Enter the room's id: ")
    if room := Room.find_by_id(id_):
        room.delete()
        print(f'Room {id_} deleted')
    else:
        print(f'Room {id_} not found')

 #implementing allocation function 

def list_allocations():
    allocations = Allocation.get_all()
    for allocation in allocations: 
        print(allocation)

def find_allocation_by_id():
    id_ = input("Enter the allocation's id: ")
    allocation = Allocation.find_by_id(id_)
    print(allocation) if allocation else print (f'Allocation {id_} not found')

def create_allocation():
    student_id = input ("Enter the allocation's student_id: ")
    room_id = input("Enter the allocation's room_id: ")
    try: 
        allocation = Allocation.create(student_id, room_id)
        print(f'Success: {allocation}')
    except Exception as exc: 
        print("Error creating allocation: ", exc)

def update_allocation():
    id_ = input("Enter the allocation's id: ")
    if allocation := Allocation.find_by_id(id_):
        try:
            student_id = input("Enter the allocation's new student_id: ")
            allocation.student_id = student_id
            room_id = input("Enter the allocation's new room_id: ")
            allocation.room_id=room_id
    
            allocation.update()
            print(f'Success: {allocation}')
        except Exception as exc:
            print("Error updating allocation: ", exc)
    else:
        print(f'Allocation {id_} not found')


def delete_allocation():
    id_ = input("Enter the allocation's id: ")
    if allocation := Allocation.find_by_id(id_):
        allocation.delete()
        print(f'Allocation {id_} deleted')
    else:
        print(f'Allocation {id_} not found')

