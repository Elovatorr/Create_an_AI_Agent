import os.path


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_directory = os.path.normpath(os.path.join(working_directory_abs, directory))
        valid_path = os.path.commonpath([working_directory_abs, target_directory]) == working_directory_abs

        if not valid_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'

        return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f"Error: {e}"