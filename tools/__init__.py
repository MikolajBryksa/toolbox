"""
Tools package - contains all individual tools/features.
Each tool should be in its own subdirectory.
"""
from flask import Flask
from typing import List, Dict


def register_tools(app: Flask) -> List[Dict[str, str]]:
    """
    Register all tools with the Flask app and return list of tools for display.
    
    Args:
        app: Flask application instance
        
    Returns:
        List of tool dictionaries with 'name', 'description', and 'url' keys
    """
    tools = []
    
    # Import and register example tool
    from tools.example_tool import register_example_tool
    example_info = register_example_tool(app)
    tools.append(example_info)
    
    # Add more tools here as you create them
    # from tools.another_tool import register_another_tool
    # another_info = register_another_tool(app)
    # tools.append(another_info)
    
    return tools
