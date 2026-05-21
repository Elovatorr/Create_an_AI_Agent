import os.path
from config import max_characters

from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the first 10000 characters of content from a file in the working directory as a string. truncates output if contents are longer that 10000 characters",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to the file to be read, relative to the working directory",
                                    ),
                                },
        required=["file_path"]
    ),
)


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_path = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs

        if not valid_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(target_file,"r") as f:
            file_content = f.read(max_characters)
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {max_characters} characters]'
                return file_content
            return file_content
    except Exception as e:
        return f"Error: {e}"