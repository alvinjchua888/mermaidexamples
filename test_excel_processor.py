"""Tests for the excel_processor module."""
import os
import pytest
import pandas as pd
from excel_processor import excel_to_html, get_sheet_names


@pytest.fixture
def sample_excel_file(tmp_path):
    """Create a sample Excel file for testing."""
    file_path = tmp_path / "test_data.xlsx"
    
    # Create sample data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)
    
    # Save to Excel
    df.to_excel(file_path, index=False, sheet_name='Sheet1')
    
    return str(file_path)


@pytest.fixture
def multi_sheet_excel_file(tmp_path):
    """Create a multi-sheet Excel file for testing."""
    file_path = tmp_path / "test_multi_sheet.xlsx"
    
    # Create sample data for multiple sheets
    data1 = {'Name': ['Alice', 'Bob'], 'Score': [85, 90]}
    data2 = {'Product': ['Widget', 'Gadget'], 'Price': [10.99, 20.99]}
    
    # Save to Excel with multiple sheets
    with pd.ExcelWriter(file_path) as writer:
        pd.DataFrame(data1).to_excel(writer, sheet_name='Students', index=False)
        pd.DataFrame(data2).to_excel(writer, sheet_name='Products', index=False)
    
    return str(file_path)


def test_excel_to_html_basic(sample_excel_file):
    """Test basic Excel to HTML conversion."""
    html = excel_to_html(sample_excel_file)
    
    # Check that HTML contains expected elements
    assert '<table' in html
    assert '</table>' in html
    assert 'Alice' in html
    assert 'Bob' in html
    assert 'Charlie' in html
    assert 'New York' in html
    assert 'table-striped' in html
    assert 'table-bordered' in html


def test_excel_to_html_with_sheet_name(multi_sheet_excel_file):
    """Test Excel to HTML conversion with specific sheet name."""
    html = excel_to_html(multi_sheet_excel_file, sheet_name='Products')
    
    # Check that HTML contains data from Products sheet
    assert 'Widget' in html
    assert 'Gadget' in html
    assert '10.99' in html
    assert '20.99' in html


def test_excel_to_html_file_not_found():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError):
        excel_to_html('/nonexistent/file.xlsx')


def test_excel_to_html_invalid_file(tmp_path):
    """Test that ValueError is raised for invalid Excel file."""
    invalid_file = tmp_path / "invalid.xlsx"
    invalid_file.write_text("This is not an Excel file")
    
    with pytest.raises(ValueError):
        excel_to_html(str(invalid_file))


def test_get_sheet_names(multi_sheet_excel_file):
    """Test getting sheet names from Excel file."""
    sheet_names = get_sheet_names(multi_sheet_excel_file)
    
    assert len(sheet_names) == 2
    assert 'Students' in sheet_names
    assert 'Products' in sheet_names


def test_get_sheet_names_single_sheet(sample_excel_file):
    """Test getting sheet names from single-sheet Excel file."""
    sheet_names = get_sheet_names(sample_excel_file)
    
    assert len(sheet_names) == 1
    assert 'Sheet1' in sheet_names


def test_get_sheet_names_file_not_found():
    """Test that FileNotFoundError is raised when getting sheet names."""
    with pytest.raises(FileNotFoundError):
        get_sheet_names('/nonexistent/file.xlsx')


def test_get_sheet_names_invalid_file(tmp_path):
    """Test that ValueError is raised for invalid Excel file."""
    invalid_file = tmp_path / "invalid.xlsx"
    invalid_file.write_text("This is not an Excel file")
    
    with pytest.raises(ValueError):
        get_sheet_names(str(invalid_file))
