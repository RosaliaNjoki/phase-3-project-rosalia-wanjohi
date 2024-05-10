from __init__ import CURSOR, CONN

class Student:

    def __init__(self, name, gender, department, id=None):
        self.id = id
        self.name = name
        self.gender = gender
        self.department = department

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value not in ['Male', 'Female']:
            raise ValueError("Gender must be either 'Male' or 'Female'.")
        self._gender = value

    def __repr__(self):
        return f"<Student {self.id}: {self.name}, {self.gender}, {self.department}>"

    @classmethod 
    def create_table(cls):
        """ Create a new table to persist the attributes of Student instances """
        sql="""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL, 
                gender TEXT NOT NULL, 
                department TEXT NOT NULL
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod 
    def drop_table(cls):
        """ Drop the table that persists Student instances """
        sql="""
            DROP TABLE IF EXISTS students;  
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, gender, and department values of the current Student instance.
        Update object id attribute using the primary key value of new row.
        """
        sql ="""
            INSERT INTO students(name, gender, department)
            VALUES (?, ?, ?)
        """   
        CURSOR.execute(sql, (self.name, self.gender, self.department))
        CONN.commit()
        self.id = CURSOR.lastrowid 

    @classmethod 
    def create(cls, name, gender, department):
         """ Initialize a new Student instance and save the object to the database """
         student = cls(name, gender, department)
         student.save()
         return student

    def update(self):
        """Update the table row corresponding to the current Student instance."""
        sql ="""
            UPDATE students 
            SET name = ?, gender = ?, department = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.gender, self.department, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Student instance"""
        sql= """
            DELETE FROM students
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def find_by_id(cls, student_id):
        """Find a student by their ID."""
        CURSOR.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        row = CURSOR.fetchone()
        if row:
            return Student(*row)  

    @classmethod 
    def get_all(cls):
        """Get all students from the database."""
        CURSOR.execute("SELECT * FROM students")
        rows = CURSOR.fetchall()
        students = []
        for row in rows:
            student = Student(*row)
            students.append(student)
        return students

    def allocate_to_room(self, room_id):
        """Allocate this student to the room with the given ID."""
        allocation = Allocation(student_id=self.id, room_id=room_id)
        allocation.save()

    def deallocate_from_room(self, room_id):
        """Deallocate this student from the room with the given ID."""
        allocations = Allocation.get_allocations_by_student_id(self.id)
        for allocation in allocations:
            if allocation.room_id == room_id:
                allocation.delete()    
