import os, subprocess


def run_python_file(working_directory, file_path, args=[]):
    try:
        working_abspath = os.path.abspath(working_directory)
        path = os.path.abspath(os.path.join(working_directory, file_path))

        if not path.startswith(working_abspath):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(path):
            return f'Error: File "{file_path}" not found.'
        
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

    except Exception as e:
        return f'Error: {e}'
    
    else:
        try:

            command = ["python", file_path] + args
            
            completed_process = subprocess.run(command, cwd=working_abspath, timeout=30, capture_output=True)

            stdout = completed_process.stdout.decode()
            stderr = completed_process.stderr.decode()

            if not stdout and not stderr:
                return "No output produced."

            output = f'STDOUT: {stdout}STDERR: {stderr}'

            if completed_process.returncode != 0:
                output += f'\nProcess exited with code {completed_process.returncode}'

            return output
        
        except Exception as e:
            return f'Error: executing Python file: {e}'
        
