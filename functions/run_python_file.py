import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        # directory validation check
        working_directory_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_path = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs
        if not valid_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]

        if args:
            command.extend(args)
        process = subprocess.run(command,cwd=working_directory_abs,capture_output=True,text=True,timeout=30)

        output_parts = []

        if process.returncode != 0:
            output_parts.append(f"Process exited with code {process.returncode}")

        if not process.stdout:
            if not process.stderr:
                output_parts.append("No output produced")
        else:
            output_parts.append(f"STDOUT: {process.stdout}")
        if process.stderr:
            output_parts.append(f"STDERR: {process.stderr}")

        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"
