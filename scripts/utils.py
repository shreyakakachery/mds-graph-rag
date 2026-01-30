import re
import os
import json

def normalize_concept(concept):
    """
    Standardizes concept strings to ensure consistency in the knowledge graph.

    This function removes punctuation, converts text to lowercase, and 
    collapses internal whitespace to prevent duplicate nodes.

    Args:
        concept (str): The raw concept string extracted by the LLM.

    Returns:
        str: A cleaned, lowercase, and normalized version of the string.

    Example:
        >>> normalize_concept(" Data   Cleaning! ")
        'data cleaning'
    """
    # Lowercase and remove leading/trailing whitespace
    clean_concept = concept.lower().strip()
    
    # Remove special characters but keep spaces and hyphens
    clean_concept = re.sub(r'[^a-z0-9\s-]', '', clean_concept)
    
    # Collapse multiple spaces into one
    clean_concept = " ".join(clean_concept.split())
    
    return clean_concept


def load_prompt(filename):
    """
    Reads the content of a prompt file from the prompts directory.

    Args:
        filename (str): The name of the file to load (e.g., 'concept_extraction.md').

    Returns:
        str: The full text content of the prompt file.

    Example:
        >>> # Assuming 'test.md' contains 'Hello World'
        >>> load_prompt('test.md')
        'Hello World'
    """
    # Build the path relative to the project root
    path = os.path.join('prompts', filename)
    
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def save_json(data, filepath):
    """
    Saves a Python dictionary to a JSON file with pretty-printing.

    This function ensures the destination directory exists before writing.
    It uses an indent of 2 for a balance between readability and file size.

    Args:
        data (dict): The dictionary or list to be saved.
        filepath (str): The destination path (e.g., 'data/processed/extractions.json').

    Example:
        >>> my_data = {"DSCI_511": ["Python", "Programming"]}
        >>> save_json(my_data, 'data/processed/test.json')
        # Created directory 'data/processed/' and saved test.json
    """
    directory = os.path.dirname(filepath)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)