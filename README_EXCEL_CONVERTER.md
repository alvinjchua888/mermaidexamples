# Excel to HTML Web Converter

A Python-based web application that converts Excel files (.xlsx, .xls) to HTML tables.

## Features

- 📊 Upload Excel files through a modern web interface
- 🎨 Beautiful Bootstrap-styled HTML tables
- 📄 Support for both .xlsx and .xls formats
- 🔄 Automatic conversion with instant results
- 🛡️ File size limit (16 MB) and type validation
- ✨ Clean and responsive UI design

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Web Application

1. Start the Flask server:

```bash
python excel_to_html_app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Upload an Excel file using the web interface

4. View the converted HTML table

### Using the Excel Processor Module Directly

You can also use the `excel_processor` module directly in your Python code:

```python
from excel_processor import excel_to_html, get_sheet_names

# Convert Excel file to HTML
html_table = excel_to_html('path/to/file.xlsx')

# Convert specific sheet
html_table = excel_to_html('path/to/file.xlsx', sheet_name='Sheet2')

# Get all sheet names
sheets = get_sheet_names('path/to/file.xlsx')
print(sheets)  # ['Sheet1', 'Sheet2', 'Sheet3']
```

## Project Structure

```
.
├── excel_to_html_app.py      # Flask web application
├── excel_processor.py         # Excel processing module
├── templates/
│   ├── index.html            # Upload page template
│   └── result.html           # Results page template
├── test_excel_processor.py   # Tests for Excel processor
├── requirements.txt          # Python dependencies
└── README_EXCEL_CONVERTER.md # This file
```

## Testing

Run the test suite:

```bash
python -m pytest test_excel_processor.py -v
```

Run all tests:

```bash
python -m pytest -v
```

## Dependencies

- Flask 3.0.0 - Web framework
- pandas 2.1.4 - Data manipulation and Excel reading
- openpyxl 3.1.2 - Excel file support
- Werkzeug 3.0.1 - WSGI utilities
- pytest 9.0.0 - Testing framework

## Configuration

The web application can be configured through the Flask app config:

- `UPLOAD_FOLDER`: Directory for temporary file uploads (default: 'uploads')
- `MAX_CONTENT_LENGTH`: Maximum file size in bytes (default: 16 MB)
- `ALLOWED_EXTENSIONS`: Allowed file extensions (default: {'xlsx', 'xls'})

## Security Notes

- Files are validated for type and size before processing
- Uploaded files are automatically deleted after conversion
- The application uses secure filename handling
- In production, change the SECRET_KEY in the Flask app

## License

This project is part of the mermaidexamples repository.
