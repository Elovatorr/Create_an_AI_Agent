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

        directory_item_names = os.listdir(target_directory)
        directory_list = []

        for item in directory_item_names:
                path_to_item = os.path.join(target_directory,item)
                item_size = os.path.getsize(path_to_item)
                #print(path_to_item, item_size)
                directory_list.append(f"- {item}: file_size={item_size} bytes, is_dir={os.path.isdir(path_to_item)}")

        complete_string = "\n".join(directory_list)

        return complete_string
    except Exception as e:
        return f"Error: {e}"