import os


def get_files_info(working_directory, directory="."):
    
    path = os.path.join(working_directory, directory)
    
    # Initial Error handling

    if not os.path.abspath(path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'

    result = ""

    try:
        contents = os.listdir(path)
        for file in contents:
            if result:
                result += '\n'
            filepath = os.path.join(path, file)
            result += f'- {file}: file_size={os.path.getsize(filepath)} bytes, is_dir={os.path.isdir(filepath)}'
    except Exception as e:
        return f'Error: Error processing {path}\n{e}'

    return result
