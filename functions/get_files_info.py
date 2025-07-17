import os


def get_files_info(working_directory, directory=None):
    
    path = os.path.join(working_directory, directory)
    
    # Error handling

    if not os.path.abspath(directory).startswith(working_directory):
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.isdir(directory):
        print(f'Error: "{directory}" is not a directory')
    
    print(os.path.abspath(directory))
    
    return path
