from __init__ import CURSOR, CONN

class Hostel:

    MAX_CAPACITY = 300  # Maximum capacity per hostel

    def __init__(self, name, capacity, id=None):
        self._id = id
        self._name = name
        self._capacity = capacity

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity must be a positive integer.")
        if value > self.MAX_CAPACITY:
            raise ValueError(f"Capacity cannot exceed {self.MAX_CAPACITY} rooms per hostel.")
        self._capacity = value

    def __repr__(self):
        return f"<Hostel {self.id}: {self.name}, {self.capacity}>"

    @classmethod 
    def create_table(cls):
        """ Create a new table to persist the attributes of Hostel instances """
        sql="""
            CREATE TABLE IF NOT EXISTS hostels (
                id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL, 
                capacity INTEGER NOT NULL
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod 
    def drop_table(cls):
        """ Drop the table that persists Hostel instances """
        sql="""
            DROP TABLE IF EXISTS hostels;  
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and capacity values of the current Hostel instance.
        Update object id attribute using the primary key value of new row.
        """
        sql ="""
            INSERT INTO hostels(name, capacity)
            VALUES (?, ?)
        """   
        CURSOR.execute(sql, (self.name, self.capacity))
        CONN.commit()
        self.id = CURSOR.lastrowid 

    @classmethod 
    def create(cls, name, capacity):
         """ Initialize a new Hostel instance and save the object to the database """
         hostel = cls(name, capacity)
         hostel.save()
         return hostel

    def update(self):
        """Update the table row corresponding to the current Hostel instance."""
        sql ="""
            UPDATE hostels 
            SET name = ?, capacity = ? 
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.capacity, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Hostel instance"""
        sql= """
            DELETE FROM hostels
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def find_by_id(cls, hostel_id):
        """Find a hostel by its ID."""
        CURSOR.execute("SELECT * FROM hostels WHERE id = ?", (hostel_id,))
        row = CURSOR.fetchone()
        if row:
            return Hostel(*row)  

    @classmethod 
    def get_all(cls):
        """Get all hostels from the database."""
        CURSOR.execute("SELECT * FROM hostels")
        rows = CURSOR.fetchall()
        hostels = []
        for row in rows:
            hostel = Hostel(*row)
            hostels.append(hostel)
        return hostels

    def get_rooms(self):
        """Get all rooms belonging to this hostel."""
        return Room.get_rooms_by_hostel_id(self.id)