# PyGround 🐍

A modular Flask-based web application for practicing and showcasing various Python tools and features. Each tool is independent and lives in its own directory, making it easy to add new functionalities.

## Features

- 🎯 **Modular Design**: Each tool is independent and self-contained
- 🔧 **Easy to Extend**: Simple structure for adding new tools
- 🎨 **Clean UI**: Responsive design with a modern interface
- 📦 **Organized Structure**: Clear separation of concerns

## Quick Start

### Prerequisites

- Python 3.7 or higher
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/MikolajBryksa/pyground.git
cd pyground
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
pyground/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── tools/                 # All tools directory
│   ├── __init__.py       # Tools registration
│   └── example_tool/     # Example tool
│       └── __init__.py
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── home.html        # Home page
│   └── tools/           # Tool-specific templates
│       └── example_tool.html
└── static/              # Static files
    └── css/
        └── style.css    # Main stylesheet
```

## Adding a New Tool

Follow these steps to add a new tool to PyGround:

### 1. Create a new tool directory

Create a new folder under `tools/` with your tool name:

```bash
mkdir tools/my_new_tool
```

### 2. Create the tool module

Create `tools/my_new_tool/__init__.py`:

```python
"""
My New Tool - Description of what it does.
"""
from flask import Flask, render_template


def register_my_new_tool(app: Flask) -> dict:
    """
    Register the tool with the Flask app.
    
    Args:
        app: Flask application instance
        
    Returns:
        Dictionary with tool information
    """
    
    @app.route('/tools/my-new-tool')
    def my_new_tool():
        """My new tool page."""
        return render_template('tools/my_new_tool.html')
    
    return {
        'name': 'My New Tool',
        'description': 'A brief description of what the tool does',
        'url': '/tools/my-new-tool'
    }
```

### 3. Create the tool template

Create `templates/tools/my_new_tool.html`:

```html
{% extends "base.html" %}

{% block title %}My New Tool - PyGround{% endblock %}

{% block content %}
<div class="tool-page">
    <h2>My New Tool</h2>
    
    <div class="tool-content">
        <!-- Your tool's content goes here -->
        <p>Welcome to my new tool!</p>
    </div>
    
    <div class="back-link">
        <a href="/" class="btn">← Back to Home</a>
    </div>
</div>
{% endblock %}
```

### 4. Register the tool

Edit `tools/__init__.py` and add your tool to the registration:

```python
def register_tools(app: Flask) -> List[Dict[str, str]]:
    tools = []
    
    # ... existing tools ...
    
    # Add your new tool
    from tools.my_new_tool import register_my_new_tool
    my_tool_info = register_my_new_tool(app)
    tools.append(my_tool_info)
    
    return tools
```

### 5. Restart the application

Stop the Flask server (Ctrl+C) and run it again:

```bash
python app.py
```

Your new tool will now appear on the home page!

## Development Tips

- Each tool should be self-contained and independent
- Use descriptive names for your tools
- Follow the existing code structure for consistency
- Add appropriate error handling in your tools
- Test your tool thoroughly before committing

## Contributing

Feel free to add your own tools and experiments!

## License

This project is for educational and practice purposes.
