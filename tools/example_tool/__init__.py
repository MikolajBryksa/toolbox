"""
Example Tool - A simple demonstration tool.
"""
from flask import Flask, render_template


def register_example_tool(app: Flask) -> dict:
    """
    Register the example tool with the Flask app.
    
    Args:
        app: Flask application instance
        
    Returns:
        Dictionary with tool information
    """
    
    @app.route('/tools/example')
    def example_tool():
        """Example tool page."""
        return render_template('tools/example_tool.html')
    
    return {
        'name': 'Example Tool',
        'description': 'A simple example tool to demonstrate the structure',
        'url': '/tools/example'
    }
