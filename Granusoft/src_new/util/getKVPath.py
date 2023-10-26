import os

def getKVPath(cwd, file):
    # Get the current file path
    current_file_path = file

    # Get the current working directory
    current_directory = cwd

    # Calculate the relative path to the current file
    relative_path = os.path.relpath(current_file_path, current_directory)

    relative_path = relative_path.replace(".py", ".kv")
    return relative_path
