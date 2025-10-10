# Template Injector

A flexible command-line tool for rendering Jinja2 templates with variables loaded from configuration files in multiple formats.

## Overview

Template Injector reads a Jinja2 template file and a variables file (supporting key-value, JSON, or YAML formats), then renders the template with the provided variables and saves the output to a specified file.

## Requirements

- Python 3.x
- Jinja2

Install dependencies:
```bash
pip install jinja2
```

Optional dependencies for YAML support:
```bash
pip install pyyaml
```

## Usage

```bash
python main.py <TEMPLATE_FILE> <OUTPUT_FILE> [OPTIONS]
```

### Arguments

- `TEMPLATE_FILE`: Path to your Jinja2 template file
- `OUTPUT_FILE`: Path where the rendered output will be saved

### Options

- `-v, --vars PATH`: Specify variables file (default: `./vars`)
- `-q, --quiet`: Reduce verbosity of output
- `-V, --version`: Show version information

### Variables File Formats

#### Key-Value Format (default)

Create a file named `vars` with `KEY=VALUE` pairs:

```
name=John Doe
email=john@example.com
version=1.0.0
```

Lines starting with `#` are treated as comments and empty lines are ignored.

#### JSON Format

Use a `.json` file extension:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "version": "1.0.0",
  "features": ["fast", "simple", "flexible"]
}
```

#### YAML Format

Use a `.yaml` or `.yml` file extension (requires PyYAML):

```yaml
name: John Doe
email: john@example.com
version: 1.0.0
features:
  - fast
  - simple
  - flexible
```

## Examples

### Example 1: Basic Usage

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

### Example 2: Using JSON Variables

**Template** (`config.txt`):
```
# Configuration for {{ project }}
{% for feature in features %}
- {{ feature }}
{% endfor %}
```

**Variables** (`config.json`):
```json
{
  "project": "MyApp",
  "features": ["Authentication", "API", "Database"]
}
```

**Command**:
```bash
python main.py config.txt output.txt -v config.json
```

### Example 3: Using YAML Variables

**Variables** (`settings.yaml`):
```yaml
server:
  host: localhost
  port: 8080
database:
  name: mydb
  user: admin
```

**Command**:
```bash
python main.py template.j2 config.conf -v settings.yaml
```

## Features

- **Multiple input formats**: Key-value pairs, JSON, and YAML
- **Full Jinja2 support**: All template features (loops, conditionals, filters, etc.)
- **Smart file handling**: Automatic format detection based on file extension
- **Error handling**: Clear error messages for template syntax and file issues
- **Flexible configuration**: Specify custom vars file location
- **Comment support**: Lines starting with `#` in key-value files are ignored
- **Quiet mode**: Suppress informational messages with `-q` flag

## File Structure

```
injector/
├── main.py          # Main script
├── imports.py       # Import statements (deprecated)
├── vars             # Default variables file (key-value format)
└── README.md        # Documentation
```

## Template Features

The tool supports all Jinja2 template features:

- **Variables**: `{{ variable_name }}`
- **Conditionals**: `{% if condition %}...{% endif %}`
- **Loops**: `{% for item in items %}...{% endfor %}`
- **Filters**: `{{ text|upper }}`, `{{ list|join(', ') }}`
- **Macros**: Reusable template snippets
- **Template inheritance**: Block and extend functionality

The environment includes:
- Auto-escaping for HTML and XML files
- Trim blocks and left-strip blocks for cleaner output

## Error Handling

The tool provides clear error messages for:
- Missing template or variables files
- Invalid template syntax
- Malformed variable files
- Missing PyYAML dependency (when using YAML files)

## Notes

- Key-value format: Lines without `=` will be skipped with a warning
- YAML support requires the `pyyaml` package
- Empty lines are ignored in all formats
- Template directory is automatically detected from the template file path

## License

No license.......... *yet*
