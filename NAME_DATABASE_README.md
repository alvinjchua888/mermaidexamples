# Name Database Module

A Python module for storing first and last names in a SQLite database.

## Features

- Store first name and last name in a SQLite database
- Interactive input prompting
- Input validation (prevents empty names)
- Automatic database initialization
- Retrieve all stored names
- Timestamps for each entry

## Usage

### Method 1: Interactive Input

Run the module directly to be prompted for names:

```bash
python3 name_database.py
```

This will prompt you to enter your first name and last name, then store them in the database.

### Method 2: Programmatic Usage

Import and use the functions in your own code:

```python
from name_database import store_name, get_all_names

# Store a name directly
record_id = store_name("John", "Doe")

# Retrieve all names
names = get_all_names()
for record in names:
    id, first_name, last_name, created_at = record
    print(f"{first_name} {last_name}")
```

### Method 3: Use the Example Script

Run the example script to see different usage patterns:

```bash
python3 example_usage.py
```

## Functions

### `store_name(first_name, last_name, db_name="names.db")`

Store a first name and last name in the database.

**Parameters:**
- `first_name` (str): The first name to store
- `last_name` (str): The last name to store
- `db_name` (str): Database file name (default: "names.db")

**Returns:**
- `int`: ID of the inserted record, or `None` if an error occurred

### `get_name_input_and_store()`

Prompt the user for first and last name, then store in the database.

**Returns:**
- `int`: ID of the inserted record, or `None` if an error occurred

### `get_all_names(db_name="names.db")`

Retrieve all names from the database.

**Parameters:**
- `db_name` (str): Database file name (default: "names.db")

**Returns:**
- `list`: List of tuples containing (id, first_name, last_name, created_at)

### `initialize_database(db_name="names.db")`

Initialize the database and create the names table if it doesn't exist.

**Parameters:**
- `db_name` (str): Database file name (default: "names.db")

**Returns:**
- `str`: Path to the database file

## Database Schema

The module creates a SQLite database with the following schema:

```sql
CREATE TABLE names (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

## Testing

Run the test suite to verify functionality:

```bash
python3 -m pytest test_name_database.py -v
```

## Requirements

- Python 3.x
- sqlite3 (included in Python standard library)
- pytest (for running tests)

## Notes

- Database file is created automatically if it doesn't exist
- Names are trimmed of leading/trailing whitespace
- Empty names (or whitespace-only) are rejected with an error message
- All database operations include error handling
- The database file is named `names.db` by default but can be customized
