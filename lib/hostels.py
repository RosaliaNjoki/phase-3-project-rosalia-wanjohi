from __init__ import CURSOR, CONN

class Hostel:

    def __init__(self, name, capacity, id=None):
        self.id = id
        self.name = name
        self.capacity = capacity

    def __repr__(self):
        return f"<Hostel {self.id}: {self.name}, {self.capacity}>"

    @classmethod 
    def create_table(cls):
        """ Create a new table to persist the attributes of Hostel instances """
        sql="""
            CREATE TABLE IF NOT EXISTS hostels
            (id INTEGER PRIMARY KEY, 
            name TEXT, 
            capacity INTEGER)
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
            INSERT INTO students(name, capacity)
            VALUES (?,?)
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
            SET name = ?, capacity=? 
            WHERE id =?
        """
        CURSOR.execute(sql, (self.name, self.capacity, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Hostel instance"""
        sql= """
            DELETE FROM hostels
            WHERe id =?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def find_by_id(db, hostel_id):
        db.cur.execute("SELECT * FROM hostels WHERE id = ?", (hostel_id,))
        row = db.cur.fetchone()
        if row:
            return Hostel(*row)  

    @classmethod 
    def get_all(db):
        db.cur.execute("SELECT * FROM hostels")
        rows = db.cur.fetchall()
        hostels = []
        for row in rows:
            hostel = Hostel(*row)
            hostels.append(hostel)
        return hostels     