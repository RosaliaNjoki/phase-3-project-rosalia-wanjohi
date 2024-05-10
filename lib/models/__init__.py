# lib/__init__.py
import sqlite3

CONN = sqlite3.connect('hostel_allocation.db')
CURSOR = CONN.cursor()