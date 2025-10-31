import builtins
import sqlite3
import os
import pytest
from name_database import (
    initialize_database,
    store_name,
    get_name_input_and_store,
    get_all_names
)


@pytest.fixture
def test_db(tmp_path):
    """Create a temporary database for testing."""
    db_path = tmp_path / "test_names.db"
    yield str(db_path)
    # Cleanup: remove the database after the test
    if os.path.exists(db_path):
        os.remove(db_path)


def test_initialize_database(test_db):
    """Test that the database is initialized correctly."""
    db_path = initialize_database(test_db)
    
    # Check that the database file was created
    assert os.path.exists(db_path)
    
    # Check that the table was created with correct schema
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='names'")
    result = cursor.fetchone()
    assert result is not None
    assert result[0] == "names"
    
    # Check table columns
    cursor.execute("PRAGMA table_info(names)")
    columns = cursor.fetchall()
    column_names = [col[1] for col in columns]
    
    assert "id" in column_names
    assert "first_name" in column_names
    assert "last_name" in column_names
    assert "created_at" in column_names
    
    conn.close()


def test_store_name_success(test_db, capsys):
    """Test storing a name successfully."""
    record_id = store_name("John", "Doe", test_db)
    
    assert record_id is not None
    assert record_id > 0
    
    captured = capsys.readouterr()
    assert "Successfully stored: John Doe" in captured.out
    assert f"(ID: {record_id})" in captured.out
    
    # Verify the name was stored in the database
    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name FROM names WHERE id = ?", (record_id,))
    result = cursor.fetchone()
    conn.close()
    
    assert result is not None
    assert result[0] == "John"
    assert result[1] == "Doe"


def test_store_name_with_whitespace(test_db, capsys):
    """Test that names with leading/trailing whitespace are trimmed."""
    record_id = store_name("  Jane  ", "  Smith  ", test_db)
    
    assert record_id is not None
    
    captured = capsys.readouterr()
    assert "Successfully stored: Jane Smith" in captured.out
    
    # Verify trimmed names in database
    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name FROM names WHERE id = ?", (record_id,))
    result = cursor.fetchone()
    conn.close()
    
    assert result[0] == "Jane"
    assert result[1] == "Smith"


def test_store_name_empty_first_name(test_db, capsys):
    """Test that empty first name is rejected."""
    record_id = store_name("", "Doe", test_db)
    
    assert record_id is None
    
    captured = capsys.readouterr()
    assert "Error: First name cannot be empty." in captured.out


def test_store_name_empty_last_name(test_db, capsys):
    """Test that empty last name is rejected."""
    record_id = store_name("John", "", test_db)
    
    assert record_id is None
    
    captured = capsys.readouterr()
    assert "Error: Last name cannot be empty." in captured.out


def test_store_name_whitespace_only_first_name(test_db, capsys):
    """Test that whitespace-only first name is rejected."""
    record_id = store_name("   ", "Doe", test_db)
    
    assert record_id is None
    
    captured = capsys.readouterr()
    assert "Error: First name cannot be empty." in captured.out


def test_store_name_whitespace_only_last_name(test_db, capsys):
    """Test that whitespace-only last name is rejected."""
    record_id = store_name("John", "   ", test_db)
    
    assert record_id is None
    
    captured = capsys.readouterr()
    assert "Error: Last name cannot be empty." in captured.out


def test_get_name_input_and_store(test_db, monkeypatch, capsys):
    """Test the interactive name input and storage function."""
    inputs = iter(['Alice', 'Johnson'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    
    record_id = get_name_input_and_store()
    
    assert record_id is not None
    assert record_id > 0
    
    captured = capsys.readouterr()
    assert "Successfully stored: Alice Johnson" in captured.out


def test_get_name_input_and_store_with_whitespace(test_db, monkeypatch, capsys):
    """Test interactive input with whitespace."""
    inputs = iter(['  Bob  ', '  Williams  '])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    
    record_id = get_name_input_and_store()
    
    assert record_id is not None
    
    captured = capsys.readouterr()
    assert "Successfully stored: Bob Williams" in captured.out


def test_get_name_input_and_store_empty_input(test_db, monkeypatch, capsys):
    """Test interactive input with empty values."""
    inputs = iter(['', 'Doe'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    
    record_id = get_name_input_and_store()
    
    assert record_id is None
    
    captured = capsys.readouterr()
    assert "Error: First name cannot be empty." in captured.out


def test_get_all_names_empty(test_db):
    """Test getting all names from an empty database."""
    initialize_database(test_db)
    names = get_all_names(test_db)
    
    assert names == []


def test_get_all_names_with_data(test_db):
    """Test retrieving all names from the database."""
    # Store some names
    id1 = store_name("John", "Doe", test_db)
    id2 = store_name("Jane", "Smith", test_db)
    id3 = store_name("Bob", "Johnson", test_db)
    
    # Retrieve all names
    names = get_all_names(test_db)
    
    assert len(names) == 3
    assert names[0][0] == id1
    assert names[0][1] == "John"
    assert names[0][2] == "Doe"
    
    assert names[1][0] == id2
    assert names[1][1] == "Jane"
    assert names[1][2] == "Smith"
    
    assert names[2][0] == id3
    assert names[2][1] == "Bob"
    assert names[2][2] == "Johnson"


def test_get_all_names_nonexistent_database():
    """Test getting names from a database that doesn't exist."""
    names = get_all_names("nonexistent_db.db")
    
    assert names == []


def test_multiple_stores(test_db):
    """Test storing multiple names in sequence."""
    id1 = store_name("Alice", "Brown", test_db)
    id2 = store_name("Charlie", "Davis", test_db)
    id3 = store_name("Eve", "Miller", test_db)
    
    assert id1 is not None
    assert id2 is not None
    assert id3 is not None
    
    # IDs should be sequential
    assert id2 == id1 + 1
    assert id3 == id2 + 1
    
    # Verify all names are in the database
    names = get_all_names(test_db)
    assert len(names) == 3
