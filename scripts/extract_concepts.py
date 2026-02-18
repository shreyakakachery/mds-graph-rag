import os
import re
import json
import subprocess
from dotenv import load_dotenv
from utils import normalize_concept, load_prompt, save_json

load_dotenv()
MODEL = os.getenv("OLLAMA_MODEL", "llama3")
RAW_DATA = "data/raw/course_descriptions.json"
OUTPUT_DATA = "data/processed/concepts.json"

def get_llm_extraction(system_prompt, course_description):
    """
    Sends the course description to Ollama and returns the extracted JSON list.
    """
    full_prompt = f"{system_prompt}\n\nCourse Description:\n{course_description}"
    
    print(f"   ...waiting for Ollama to respond...")

    process = subprocess.run(
        ['ollama', 'run', MODEL, full_prompt],
        capture_output=True, 
        text=True, 
        encoding='utf-8'
    )
    
    if process.returncode != 0:
        print(f"Error calling Ollama: {process.stderr}")
        return None
        
    return process.stdout.strip()

def main():
    system_prompt = load_prompt("concept_extraction.md")
    
    with open(RAW_DATA, 'r') as f:
        courses = json.load(f)

    extracted_data = {}

    print(f"Starting extraction with {MODEL}...")

    for course_id, details in courses.items():
        name = details.get('name', 'Unknown Course')
        description = details.get('description', '')

        print(f"Processing {course_id}: {name}...")

        if not description:
            print(f"Skipping {course_id} because description is empty.")
            continue
        
        raw_output = get_llm_extraction(system_prompt, description)
        
        if raw_output:
            try:
                match = re.search(r'\[.*\]', raw_output, re.DOTALL)
                if match:
                    clean_output = match.group(0)
                    concepts = json.loads(clean_output)
                    
                    cleaned = [normalize_concept(c) for c in concepts]
                    extracted_data[course_id] = cleaned
                    print(f"Extracted {len(cleaned)} concepts.")
                else:
                    print(f"Could not find a JSON list in the output for {course_id}.")
                
            except json.JSONDecodeError:
                print(f"Failed to parse JSON for {course_id}.")

    save_json(extracted_data, OUTPUT_DATA)
    print(f"\nDone! Results saved to {OUTPUT_DATA}")

if __name__ == "__main__":
    main()