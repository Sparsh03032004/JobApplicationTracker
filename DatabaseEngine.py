import sqlite3
import os

DB_NAME = "app_database.db"

def initialize_database():
    """Creates the SQLite database file and the applications tracking table if it doesn't exist."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    # Create the core relational tracking table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            status TEXT NOT NULL,
            interview_date TEXT,
            notes TEXT
        )
    """)
    
    connection.commit()
    connection.close()

def add_application(company, role, status, interview_date="", notes=""):
    """Inserts a new job application log into the database."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    cursor.execute("""
        INSERT INTO applications (company, role, status, interview_date, notes)
        VALUES (?, ?, ?, ?, ?)
    """, (company, role, status, interview_date, notes))
    
    connection.commit()
    connection.close()

def fetch_all_applications():
    """Retrieves all tracked applications sorted by upcoming interview dates."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM applications ORDER BY interview_date ASC")
    rows = cursor.fetchall()
    
    connection.close()
    return rows

def delete_application(app_id):
    """Removes a specific record from the dashboard using its unique ID row primary key."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM applications WHERE id = ?", (app_id,))
    
    connection.commit()
    connection.close()