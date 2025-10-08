# Template Injector

A simple command-line tool for rendering Jinja2 templates with variables loaded from a configuration file.

## Overview

Template Injector reads a Jinja2 template file and a variables file, then renders the template with the provided variables and saves the output to a specified file.

## Requirements

- Python 3.x
- Jinja2

Install dependencies:
```bash
pip install jinja2
```

## Usage

```bash
python main.py <TEMPLATE_FILE> <OUTPUT_FILE>
```

### Arguments

- `TEMPLATE_FILE`: Path to your Jinja2 template file
- `OUTPUT_FILE`: Path where the rendered output will be saved

### Variables File

Create a file named `vars` in the same directory as `main.py`. This file contains your template variables in `KEY=VALUE` format:

```
name=John Doe
email=john@example.com
version=1.0.0
```

## Example

**1. Create a template file** (`template.txt`):
```
Hello {{ name }}!
Your email is: {{ email }}
Version: {{ version }}
```

**2. Create a variables file** (`vars`):
```
name=Alice
email=alice@example.com
version=2.1.0
```

**3. Run the injector**:
```bash
python main.py template.txt output.txt
```

**4. Check the output** (`output.txt`):
```
Hello Alice!
Your email is: alice@example.com
Version: 2.1.0
```

## Features

- Simple key-value variable configuration
- Full Jinja2 template syntax support
- Automatic handling of empty lines in variables file
- Clear error messages for invalid parameter formats

## File Structure

```
injector/
├── main.py          # Main script
├── imports.py       # Import statements
├── vars             # Variables configuration file
└── README.md        # This file
```

## Notes

- Lines in the `vars` file that don't contain an `=` sign will be skipped with a warning message
- Empty lines in the `vars` file are ignored
- All Jinja2 template features (loops, conditionals, filters, etc.) are supported

## License

No license.......... *yet*
