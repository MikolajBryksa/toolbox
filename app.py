"""
Main Flask application for PyGround - a collection of practice tools.
"""
from flask import Flask, render_template
from tools import register_tools

app = Flask(__name__)

# Note: For production deployment, set a secure secret key:
# app.secret_key = os.environ.get('SECRET_KEY') or 'your-secret-key-here'

# Register all tools
tools_list = register_tools(app)


@app.route('/')
def home():
    """Home page showing list of available tools."""
    return render_template('home.html', tools=tools_list)


if __name__ == '__main__':
    # Debug mode is enabled for development purposes
    # For production, use a WSGI server like gunicorn and set debug=False
    app.run(debug=True, host='0.0.0.0', port=5000)
