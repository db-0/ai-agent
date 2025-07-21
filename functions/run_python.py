import os


def run_python_file(working_directory, file_path, args=[]):
    try:
        working_abspath = os.path.abspath(working_directory)
        path = os.path.abspath(os.path.join(working_directory, file_path))

        if not path.startswith(working_abspath):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'


    except Exception as e:
        pass
