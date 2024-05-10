

from helper import (
    exit_program,
    list_students,
    find_student_by_name,
    find_student_by_id,
    create_student,
    update_student,
    delete_student,
    list_hostels,
    find_hostel_by_name,
    find_hostel_by_id,
    create_hostel,
    update_hostel,
    delete_hostel,
    list_rooms,
    find_room_by_room_number,
    find_room_by_id,
    create_room,
    update_room,
    delete_room,
    list_allocations,
    find_allocation_by_id,
    create_allocation,
    update_allocation,
    delete_allocation,
    list_hostel_allocations,
    list_room_allocations
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
            find_student_by_name()
        elif choice == "3":
            find_student_by_id()
        elif choice == "4":
            create_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            list_hostels()
        elif choice == "8":
            find_hostel_by_name()
        elif choice == "9":
            find_hostel_by_id()
        elif choice == "10":
            create_hostel()
        elif choice == "11":
            update_hostel()
        elif choice == "12":
            delete_employee()
        elif choice == "13":
            list_rooms()
        elif choice == "14":
            find_room_by_room_number()
        elif choice == "15":
            find_room_by_id()
        elif choice == "16":
            create_room()
        elif choice == "17":
            update_room()
        elif choice == "18":
            delete_room()
        elif choice == "19":
            list_allocations()
        elif choice == "20":
            find_allocation_by_id()
        elif choice == "21":
            create_allocation()
        elif choice == "22":
            update_allocation()
        elif choice == "23":
            delete_allocation()
        elif choice == "13":
            list_hostel_allocations()
        elif choice == "25":
            list_room_allocations()   
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all students")
    print("2. Find student by name")
    print("3. Find student by id")
    print("4: Create student ")
    print("5: Update student")
    print("6: Delete student")
    print("7. List all hostels")
    print("8. Find hostel by name")
    print("9. Find hostel by id")
    print("10: Create hostel")
    print("11: Update hostel")
    print("12: Delete hostel")
    print("13. List all rooms")
    print("14. Find room by room_number")
    print("15. Find room by id")
    print("16: Create room ")
    print("17: Update room")
    print("18: Delete room")
    print("19. List all allocations")
    print("20. Find allocation by id")
    print("21: Create allocation")
    print("22: Update allocation")
    print("23: Delete allocation")
    print("24: List all allocations in a hostel")
    print("25: List all allocations in a room")


if __name__ == "__main__":
    main()

