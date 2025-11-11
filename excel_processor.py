"""Module for processing Excel files and converting them to HTML tables."""
import pandas as pd
from typing import Optional


def excel_to_html(file_path: str, sheet_name: Optional[str] = None) -> str:
    """
    Convert an Excel file to an HTML table.
    
    Args:
        file_path: Path to the Excel file
        sheet_name: Name of the sheet to convert (default: first sheet)
        
    Returns:
        HTML string containing the table
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file is not a valid Excel file
    """
    try:
        # Read Excel file
        if sheet_name:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
        else:
            df = pd.read_excel(file_path)
        
        # Convert to HTML with Bootstrap classes for styling
        html_table = df.to_html(
            classes='table table-striped table-bordered table-hover',
            index=False,
            border=0,
            na_rep='N/A'
        )
        
        return html_table
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise ValueError(f"Error processing Excel file: {str(e)}")


def get_sheet_names(file_path: str) -> list:
    """
    Get all sheet names from an Excel file.
    
    Args:
        file_path: Path to the Excel file
        
    Returns:
        List of sheet names
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file is not a valid Excel file
    """
    try:
        excel_file = pd.ExcelFile(file_path)
        return excel_file.sheet_names
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise ValueError(f"Error reading Excel file: {str(e)}")
