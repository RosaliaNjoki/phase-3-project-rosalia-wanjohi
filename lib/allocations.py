from __init__ import CURSOR, CONN

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
            CREATE TABLE IF NOT EXISTS allocations
            (id INTEGER PRIMARY KEY, 
            student_id INTEGER NOT NULL,  
            room_id INTEGER NOT NULL)
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (room_id) REFERENCES rooms(id)
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

    def save(self):
        """ Insert a new row with the student_id and room_id values of the current Allocation instance.
        Update object id attribute using the primary key value of new row.
        """
        sql ="""
            INSERT INTO allocations(student_id, room_id)
            VALUES (?,?)
        """   

        CURSOR.execute(sql, (self.student_id, self.room_id))
        CONN.commit()
        self.id = CURSOR.lastrowid 

    @classmethod 
    def create(cls, room_student_id, room_id):
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
            WHERe id =?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def find_by_id(db, allocation_id):
        db.cur.execute("SELECT * FROM allocations WHERE id = ?", (allocation_id,))
        row = db.cur.fetchone()
        if row:
            return Allocation(*row)  

    @classmethod 
    def get_all(db):
        db.cur.execute("SELECT * FROM allocations")
        rows = db.cur.fetchall()
        allocations = []
        for row in rows:
            allocation = Allocation(*row)
            allocations.append(allocation)
        return allocations 