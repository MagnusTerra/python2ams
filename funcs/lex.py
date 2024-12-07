from whats_that_code.election import guess_language_all_methods

def detect_language(code_snippet, filename=None):
    try:
        programming_code = guess_language_all_methods(code_snippet)
        
        if programming_code == filename :
            return {
                "status" : True,
                "content" : programming_code
            }
        
        else :
            return {
                "status" : False,
                "content" : f"Mismatch:Detected {programming_code} expected {filename}"
            }
            
    except Exception as e:
        return {f'An unexpecteed error have ocurred: {e}'}
        



def clean_asm_code(input_code: str) -> str:
    """
    Cleans out the ```asm and ``` markers from the provided code string.
    Args:
        input_code: A multi-line string that includes asm-like markers.
    
    Returns:
        The cleaned-up string without ```asm or ``` markers.
    """
    # Split the string by lines and clean markers
    cleaned_lines = []
    for line in input_code.splitlines():
        # Remove ```asm or ```
        if line.strip() not in ["```asm", "```"]:
            cleaned_lines.append(line)
    
    # Combine the cleaned-up lines back into a single string
    return "\n".join(cleaned_lines)


