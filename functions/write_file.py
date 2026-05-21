import os
from google.genai import types
# function declaration for gemini to read
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Creates a file in final directory in file_path with the name specified in file_path and writes content into that file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to the file to be created and written to. This will create the necessary directory if it doesnt exist and is relative to the working directory"),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to be written inside file"),
                                            },
        required=["file_path","content"]
    ),
)

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        # directory validation check
        working_directory_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_path = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs
        if not valid_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        #create directories if necessary and write file
        parent_dir = os.path.dirname(target_file)
        os.makedirs(parent_dir, exist_ok=True)
        with open(target_file,"w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
