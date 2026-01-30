import re

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