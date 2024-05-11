

from helper import (
    exit_program,
    list_students,
    find_student_by_id,
    create_student,
    update_student,
    delete_student,
    list_hostels,
    find_hostel_by_id,
    create_hostel,
    update_hostel,
    delete_hostel,
    list_rooms,
    find_room_by_id,
    create_room,
    update_room,
    delete_room,
    list_allocations,
    find_allocation_by_id,
    create_allocation,
    update_allocation,
    delete_allocation,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_students()
        elif choice == "2":
            find_student_by_id()
        elif choice == "3":
            create_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            list_hostels()
        elif choice == "7":
            find_hostel_by_id()
        elif choice == "8":
            create_hostel()
        elif choice == "9":
            update_hostel()
        elif choice == "10":
            delete_employee()
        elif choice == "11":
            list_rooms()
        elif choice == "12":
            find_room_by_id()
        elif choice == "13":
            create_room()
        elif choice == "14":
            update_room()
        elif choice == "15":
            delete_room()
        elif choice == "16":
            list_allocations()
        elif choice == "17":
            find_allocation_by_id()
        elif choice == "18":
            create_allocation()
        elif choice == "19":
            update_allocation()
        elif choice == "20":
            delete_allocation()  
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all students")
    print("2. Find student by id")
    print("3: Create student ")
    print("4: Update student")
    print("5: Delete student")
    print("6. List all hostels")
    print("7. Find hostel by id")
    print("8: Create hostel")
    print("9: Update hostel")
    print("10: Delete hostel")
    print("11. List all rooms")
    print("12. Find room by id")
    print("13: Create room ")
    print("14: Update room")
    print("15: Delete room")
    print("16. List all allocations")
    print("17. Find allocation by id")
    print("18: Create allocation")
    print("19: Update allocation")
    print("20: Delete allocation")


if __name__ == "__main__":
    main()

