import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        working_abspath = os.path.abspath(working_directory)
        path = os.path.abspath(os.path.join(working_directory, file_path))

        if not path.startswith(working_abspath):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
        with open(path, "r") as f:
            file_content = f.read(MAX_CHARS)
        
        trunc_msg = f'...File "{file_path} truncated at {MAX_CHARS} characters]'

        if len(file_content) == MAX_CHARS:
            file_content += trunc_msg
        
        return file_content
    
    
    except Exception as e:
        return f'Error: {e}'
