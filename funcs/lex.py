from pygments.lexers import guess_lexer, guess_lexer_for_filename, find_lexer_class_by_name
from pygments.util import ClassNotFound

from pygments.lexers import guess_lexer, guess_lexer_for_filename, find_lexer_class_by_name
from pygments.util import ClassNotFound

def detect_language(code_snippet, filename=None):
    try:
        # Guess the lexer using the filename if provided
        if filename:
            lexer = guess_lexer_for_filename(filename, code_snippet)
        else:
            lexer = guess_lexer(code_snippet)

        # Validate using file extension
        if filename:
            file_extension = filename.split('.')[-1].lower()
            expected_lexer = find_lexer_class_by_name(file_extension)
            if expected_lexer and expected_lexer.name != lexer.name:
                return {"status": False, 
                        "content": f"Mismatch: Detected {lexer.name} but expected {expected_lexer.name}"}

        return {"status": True, 
                "content": lexer.name}

    except ClassNotFound:
        return {"status": False, 
                "content": "Could not detect the programming language."}
    except Exception as e:
        return {"status": False, 
                "content": f"An error occurred: {str(e)}"}


# Example Usage
java_code = """
class Test
{
    public static void main(String []args)
    {
        System.out.println("My First Java Program.");
    }
};
"""

detected_language = detect_language(java_code, filename="example.js")
print(f"Detected Language: {detected_language}")
