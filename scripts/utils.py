import re
import os

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