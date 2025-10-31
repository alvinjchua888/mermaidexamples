import sqlite3
import os


def initialize_database(db_name="names.db"):
    """
    Initialize the SQLite database and create the names table if it doesn't exist.
    
    Args:
        db_name (str): Name of the database file. Defaults to "names.db"
    
    Returns:
        str: Path to the database file
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS names (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    
    return db_name


def store_name(first_name, last_name, db_name="names.db"):
    """
    Store a first name and last name in the SQLite database.
    
    Args:
        first_name (str): The first name to store
        last_name (str): The last name to store
        db_name (str): Name of the database file. Defaults to "names.db"
    
    Returns:
        int: The ID of the inserted record, or None if an error occurred
    """
    try:
        # Validate inputs
        if not first_name or not first_name.strip():
            print("Error: First name cannot be empty.")
            return None
        
        if not last_name or not last_name.strip():
            print("Error: Last name cannot be empty.")
            return None
        
        # Initialize database if it doesn't exist
        initialize_database(db_name)
        
        # Insert the name
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO names (first_name, last_name) VALUES (?, ?)",
            (first_name.strip(), last_name.strip())
        )
        
        record_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        print(f"Successfully stored: {first_name.strip()} {last_name.strip()} (ID: {record_id})")
        return record_id
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_name_input_and_store():
    """
    Prompt the user for first name and last name, then store them in the database.
    
    Returns:
        int: The ID of the inserted record, or None if an error occurred
    """
    try:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        
        return store_name(first_name, last_name)
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_all_names(db_name="names.db"):
    """
    Retrieve all names from the database.
    
    Args:
        db_name (str): Name of the database file. Defaults to "names.db"
    
    Returns:
        list: List of tuples containing (id, first_name, last_name, created_at)
    """
    try:
        if not os.path.exists(db_name):
            return []
        
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, first_name, last_name, created_at FROM names ORDER BY id")
        names = cursor.fetchall()
        
        conn.close()
        return names
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []


# Example usage
if __name__ == "__main__":
    get_name_input_and_store()
