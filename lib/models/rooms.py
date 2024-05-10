from models.__init__ import CURSOR, CONN
from models.hostels import Hostel

class Room:

    MAX_CAPACITY_PER_ROOM = 4  # Maximum bedspace per room

    def __init__(self, room_number, capacity, hostel_id, id=None):
        self._id = id
        self._room_number = room_number
        self._capacity = capacity
        self._hostel_id = hostel_id

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity must be a positive integer.")
        if value > self.MAX_CAPACITY_PER_ROOM:
            raise ValueError(f"Capacity cannot exceed {self.MAX_CAPACITY_PER_ROOM} beds per room.")
        self._capacity = value

    def __repr__(self):
        return f"<Room {self.id}: {self.room_number}, {self.capacity}, {self.hostel_id}>"

    @classmethod 
    def create_table(cls):
        """ Create a new table to persist the attributes of Room instances """
        sql="""
            CREATE TABLE IF NOT EXISTS rooms (
                id INTEGER PRIMARY KEY, 
                room_number TEXT NOT NULL, 
                capacity INTEGER, 
                hostel_id INTEGER,
                FOREIGN KEY (hostel_id) REFERENCES hostels(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod 
    def drop_table(cls):
        """ Drop the table that persists Room instances """
        sql="""
            DROP TABLE IF EXISTS rooms;  
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, room_number, capacity and hostel_id values of the current Room instance.
        Update object id attribute using the primary key value of new row.
        """
        sql ="""
            INSERT INTO rooms(room_number, capacity, hostel_id)
            VALUES (?,?, ?)
        """   
        CURSOR.execute(sql, (self.room_number, self.capacity, self.hostel_id))
        CONN.commit()
        self.id = CURSOR.lastrowid 

    @classmethod 
    def create(cls, room_number, capacity, hostel_id):
         """ Initialize a new Room instance and save the object to the database """
         room = cls(room_number, capacity, hostel_id)
         room.save()
         return room

    def update(self):
        """Update the table row corresponding to the current Room instance."""
        sql ="""
            UPDATE rooms 
            SET room_number = ?, capacity=?, hostel_id =?
            WHERE id =?
        """
        CURSOR.execute(sql, (self.room_number, self.capacity, self.hostel_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Room instance"""
        sql= """
            DELETE FROM rooms
            WHERE id =?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def find_by_id(cls, room_id):
        """Find a room by its ID."""
        CURSOR.execute("SELECT * FROM rooms WHERE id = ?", (room_id,))
        row = CURSOR.fetchone()
        if row:
            return Room(*row)

    @classmethod 
    def get_all(cls):
        """Get all rooms from the database."""
        CURSOR.execute("SELECT * FROM rooms")
        rows = CURSOR.fetchall()
        rooms = []
        for row in rows:
            room = Room(*row)
            rooms.append(room)
        return rooms

    @classmethod
    def get_rooms_by_hostel_id(cls, hostel_id):
        """Get all rooms belonging to the hostel with the given ID."""
        CURSOR.execute("SELECT * FROM rooms WHERE hostel_id = ?", (hostel_id,))
        rows = CURSOR.fetchall()
        rooms = []
        for row in rows:
            room = Room(*row)
            rooms.append(room)
        return rooms

    def add_student(self, student_id):
        """Add a student with the given ID to this room."""
        allocation = Allocation(student_id=student_id, room_id=self.id)
        allocation.save()

    def remove_student(self, student_id):
        """Remove a student with the given ID from this room."""
        allocations = Allocation.get_allocations_by_room_id(self.id)
        for allocation in allocations:
            if allocation.student_id == student_id:
                allocation.delete()    