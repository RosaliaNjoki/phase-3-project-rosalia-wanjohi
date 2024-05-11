# Hostel Management System 
The Hostel Management System is a Python application designed to manage students, hostels, rooms, and allocations within a school or university environment. This system allows administrators to perform various tasks such as adding, updating, and deleting students, hostels, rooms, and allocations. It provides functionalities for managing the allocation of students to rooms within different hostels. Overall, the Hostel Management System provides a comprehensive solution for efficiently managing student accommodation and hostel operations. Its flexible and scalable design, coupled with intuitive user interfaces and robust data management features, makes it an ideal choice for educational institutions and hostel administrator
## Functionality
### Student Management
-	Add Student: Allows administrators to add new students to the system by providing details such as name, gender, and department.
-	Update Student: Enables administrators to update existing student records, including modifying the student's name, gender, or department.
-	Delete Student: Provides the ability to remove a student from the system, including all related allocations.
### Hostel Management
-	Add Hostel: Allows administrators to create new hostels within the system, specifying the name and maximum capacity of each hostel.
-	Update Hostel: Enables administrators to modify existing hostel records, including changing the hostel's name or maximum capacity.
-	Delete Hostel: Provides the ability to remove a hostel from the system, including all related rooms and allocations.
### Room Management
-	Add Room: Allows administrators to add new rooms to a hostel, specifying the room number and capacity.
-	Update Room: Enables administrators to modify existing room records, including changing the room number or capacity.
-	Delete Room: Provides the ability to remove a room from the system, including all related allocations.
### Allocation Management
-	Allocate Student: Allows administrators to assign students to specific rooms within a hostel, ensuring efficient management of accommodation.
-	Update Allocation: Enables administrators to modify existing allocations, allowing for changes in student-room assignments.
-	Delete Allocation: Provides the ability to remove a student's allocation from a room, allowing for reassignment or removal.
## Features
### Flexible Data Management
-	Database Persistence: All data is stored in a relational database, ensuring data integrity and enabling efficient retrieval and manipulation of records.
-	Data Validation: Input data is validated to ensure accuracy and consistency, preventing errors and maintaining data integrity.
### Intuitive User Interface
-	Menu-Driven Interface: The system features a user-friendly menu-driven interface, allowing administrators to easily navigate through different functionalities and perform tasks efficiently.
-	Error Handling: The system includes robust error handling mechanisms to gracefully handle exceptions and provide informative error messages to users.
### Scalability and Extensibility
-	Modular Design: The system is designed with modularity in mind, making it easy to extend and add new features in the future.
-	Customization: Administrators can customize the system to suit their specific requirements by adding new functionalities or modifying existing ones as needed.
### Relationship and Constraints 
####	One-to-Many Relationships 
1.	Student to Allocation
  -	Allocation of Students: Each student can be allocated to one or more rooms, representing a one-to-many relationship between students and allocations.
  -	Deallocation of Students: Students can be deallocated from rooms, allowing for changes in accommodation or room assignments.
2.	Hostel to Room
  -	Rooms in Hostel: Each hostel can contain multiple rooms, representing a one-to-many relationship between hostels and rooms.
####	Many-to-Many Relationships
1. Student to Room (through Allocation)
 - Student-Room Association: Through allocations, many students can be associated with many rooms, representing a many-to-many relationship between students and rooms.
 -	Dynamic Allocation: Students can be allocated to different rooms over time, allowing for flexible accommodation arrangements.
 ####	Foreign Key Constraints
1. Hostel and Room
 -	Foreign Key Constraint: The room table contains a foreign key reference to the hostel table, ensuring that each room is associated with a specific hostel.
 - Data Integrity: Maintains data integrity by preventing orphaned records and ensuring that rooms are always linked to valid hostels.
2. Student and Allocation
  -	Foreign Key Constraint: The allocation table contains foreign key references to both the student and room tables, ensuring that each allocation is associated with a valid student and room.
  -	Data Consistency: Ensures that allocations always point to existing student and room records, preventing inconsistencies in the data.
## Technologies 
-	Python 3
-	SQLite 3
-	VSCode 
## Implementation

The project can be implemented in Python using ORM to represent the models and their relationships and connect them to the SQLite database. Each model can have methods to perform various operations, creating, deleting, updating, finding students, hostels, rooms, and allocations data. 
## Instructions

1.	Clone the repository: ```git clone git@github.com:RosaliaNjoki/phase-3-project-rosalia-wanjohi.git```
2.	Navigate to the project directory: cd ``` phase-3-project-rosalia-wanjohi```
3.	run pipenv install and then pipenv shell
4.	type ```code .``` on the terminal to navigate to the VSCode.
5.	Explore the functionalities implemented for each model and CLI.
## Configuration
To learn the app, one only needs to have basics such as Python and VSCode installed. One can also install pipenv and run pipenv shell after cloning to build a virtual environment and install dependencies. Python script should be executed in the virtual environment.
## Contributors
-	The project is created by Rosalia Njoki’
## License
This app has MIT License Copyright (c) [2024] to Rosalia Njoki Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

