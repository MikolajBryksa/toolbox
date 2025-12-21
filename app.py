"""
Main Flask application for PyGround - a collection of practice tools.
"""
from flask import Flask, render_template
from tools import register_tools

app = Flask(__name__)

# Register all tools
tools_list = register_tools(app)


@app.route('/')
def home():
    """Home page showing list of available tools."""
    return render_template('home.html', tools=tools_list)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
