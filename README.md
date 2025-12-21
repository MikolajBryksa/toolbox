# Python Playground

A modular web application designed for practicing and showcasing various Python tools and features. Each tool is independent and lives in its own directory, making it easy to add new functionalities and experiment with different Python concepts. The application provides a clean interface for accessing multiple tools from a single platform.

## Tech Stack

- **Python** 3.7 or higher
- **Flask** web framework
- **HTML/CSS** for frontend templates

## Features

- Modular design with independent and self-contained tools
- Simple structure for adding new tools
- Responsive design with a modern interface
- Clear separation of concerns with organized project structure
- Tool registration system for easy integration
- Base template system for consistent UI across tools

## Setup

### Requirements

Before you begin, ensure you have met the following requirements:

- **Python**: 3.7 or higher

  ```
  python --version
  ```

- **pip**: Latest version

  ```
  pip --version
  ```

### Installation

- **Clone the repository**:

  ```
  git clone https://github.com/MikolajBryksa/pyground.git
  ```

- **Navigate to the project directory**:

  ```
  cd pyground
  ```

- **Install dependencies**:

  ```
  pip install -r requirements.txt
  ```

### Launch

- **Run the application**:

  ```
  python app.py
  ```

- **Open your browser and navigate to**:

  ```
  http://localhost:5000
  ```

## Development

- **Create tool directory**:

  ```
  mkdir tools/my_new_tool
  ```

- **Create the tool module**:

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

- **Create the tool template**:

  Create `templates/tools/my_new_tool.html`:

  ```html
  {% extends "base.html" %} {% block title %}My New Tool - PyGround{% endblock
  %} {% block content %}
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

- **Register the tool**:

  Edit `tools/__init__.py`:

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

- **Restart the application**:

  ```
  Stop the Flask server with Ctrl+C and run python app.py again
  ```
