from models.__init__ import CURSOR, CONN
from models.rooms import Room
from models.students import Student

class Allocation:

    def __init__(self, student_id, room_id, id=None):
        self.id = id
        self.student_id = student_id
        self.room_id = room_id

    def __repr__(self):
        return f"<Allocation {self.id}: {self.student_id}, {self.room_id}>"

    @classmethod 
    def create_table(cls):
        """ Create a new table to persist the attributes of Allocation instances """
        sql="""
            CREATE TABLE IF NOT EXISTS allocations (
                id INTEGER PRIMARY KEY, 
                student_id INTEGER NOT NULL,  
                room_id INTEGER NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students(id),
                FOREIGN KEY (room_id) REFERENCES rooms(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod 
    def drop_table(cls):
        """ Drop the table that persists Allocation instances """
        sql="""
            DROP TABLE IF EXISTS allocations;  
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod 
    def create(cls, student_id, room_id):
        """ Initialize a new Allocation instance and save the object to the database """
        allocation = cls(student_id, room_id)
        allocation.save()
        return allocation

    def update(self):
        """Update the table row corresponding to the current Allocation instance."""
        sql ="""
            UPDATE allocations 
            SET student_id = ?, room_id=?
            WHERE id =?
        """
        CURSOR.execute(sql, (self.student_id, self.room_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Allocation instance"""
        sql= """
            DELETE FROM allocations
            WHERE id =?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def find_by_id(cls, allocation_id):
        """Find an allocation by its ID."""
        CURSOR.execute("SELECT * FROM allocations WHERE id = ?", (allocation_id,))
        row = CURSOR.fetchone()
        if row:
            return Allocation(*row)

    @classmethod 
    def get_all(cls):
        """Get all allocations from the database."""
        CURSOR.execute("SELECT * FROM allocations")
        rows = CURSOR.fetchall()
        allocations = []
        for row in rows:
            allocation = Allocation(*row)
            allocations.append(allocation)
        return allocations

    @classmethod
    def get_allocations_by_student_id(cls, student_id):
        """Get all room allocations for the student with the given ID."""
        CURSOR.execute("SELECT * FROM allocations WHERE student_id = ?", (student_id,))
        rows = CURSOR.fetchall()
        allocations = []
        for row in rows:
            allocation = Allocation(*row)
            allocations.append(allocation)
        return allocations

    @classmethod
    def get_allocations_by_room_id(cls, room_id):
        """Get all student allocations for the room with the given ID."""
        CURSOR.execute("SELECT * FROM allocations WHERE room_id = ?", (room_id,))
        rows = CURSOR.fetchall()
        allocations = []
        for row in rows:
            allocation = Allocation(*row)
            allocations.append(allocation)
        return allocations  

    @classmethod
    def reassign(cls, student_id, new_room_id):
        """
        Reassigns a student to a new room by removing their current allocation (if any) and saving a new one
        """
        existing_allocations = Allocation.get_allocations_by_student_id(self.student_id)
        if existing_allocations: 
            raise ValueError("Student is already allocated to another room.")

        sql = """
            INSERT INTO allocations(student_id, room_id)
            VALUES (?,?)
        """    
        CURSOR.execute(sql, (self.student_id, self.room_id))
        CONN.commit()
        self.id = CURSOR.lastrowid

        
    def save(self):
        """ 
        Insert a new row with the student_id and room_id values of the current Allocation instance.
        Update object id attribute using the primary key value of new row.
        """
        # Check if the student is already allocated to another room
        existing_allocation = Allocation.get_allocations_by_student_id(self.student_id)
        if existing_allocation:
            raise ValueError("Student is already allocated to another room.")

        # If not allocated, proceed with saving the new allocation
        sql ="""
            INSERT INTO allocations(student_id, room_id)
            VALUES (?,?)
        """   
        CURSOR.execute(sql, (self.student_id, self.room_id))
        CONN.commit()
        self.id = CURSOR.lastrowid


          
