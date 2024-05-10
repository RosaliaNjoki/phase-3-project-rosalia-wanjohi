from __init__ import CURSOR, CONN

class Room:

    def __init__(self, room_number, capacity, hostel_id, id=None):
        self.id = id
        self.room_number = room_number
        self.capacity = capacity
        self.hostel_id = hostel_id

    def __repr__(self):
        return f"<Room {self.id}: {self.room_number}, {self.capacity}, {self.hostel_id}>"

    @classmethod 
    def create_table(cls):
        """ Create a new table to persist the attributes of Room instances """
        sql="""
            CREATE TABLE IF NOT EXISTS rooms
            (id INTEGER PRIMARY KEY, 
            room_number TEXT NOT NULL, 
            capacity INTEGER, 
            hostel_id INTEGER)
            FOREIGN KEY (hostel_id) REFERENCES hostels(id)
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
            WHERe id =?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def find_by_id(db, room_id):
        db.cur.execute("SELECT * FROM rooms WHERE id = ?", (room_id,))
        row = db.cur.fetchone()
        if row:
            return Room(*row)  

    @classmethod 
    def get_all(db):
        db.cur.execute("SELECT * FROM rooms")
        rows = db.cur.fetchall()
        rooms = []
        for row in rows:
            room = Room(*row)
            rooms.append(room)
        return rooms     