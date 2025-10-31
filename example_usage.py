#!/usr/bin/env python3
"""
Example script demonstrating how to use the name_database module.

This script shows different ways to interact with the SQLite database:
1. Store names directly using the store_name function
2. Store names interactively using get_name_input_and_store
3. Retrieve and display all stored names
"""

from name_database import store_name, get_name_input_and_store, get_all_names


def example_direct_storage():
    """Example: Store names directly without user input."""
    print("=== Example 1: Direct Storage ===")
    
    # Store names directly
    store_name("Alice", "Anderson")
    store_name("Bob", "Brown")
    store_name("Charlie", "Chen")
    
    print()


def example_interactive_storage():
    """Example: Store names with user input."""
    print("=== Example 2: Interactive Storage ===")
    print("Please enter a name to store in the database:")
    get_name_input_and_store()
    print()


def example_retrieve_all():
    """Example: Retrieve and display all stored names."""
    print("=== Example 3: Retrieve All Names ===")
    
    names = get_all_names()
    
    if not names:
        print("No names found in the database.")
    else:
        print(f"Found {len(names)} name(s) in the database:")
        print("-" * 60)
        for name_record in names:
            record_id, first_name, last_name, created_at = name_record
            print(f"ID: {record_id:3d} | {first_name:15s} {last_name:15s} | {created_at}")
        print("-" * 60)
    
    print()


if __name__ == "__main__":
    print("Name Database Example Script")
    print("=" * 60)
    print()
    
    # Uncomment the examples you want to run:
    
    # Example 1: Store names directly
    # example_direct_storage()
    
    # Example 2: Store names interactively
    # example_interactive_storage()
    
    # Example 3: Display all stored names
    example_retrieve_all()
