# lib/file_io.py

def write_file(file_name, file_content):
    """Writes content to a .txt file. Creates a new file or overwrites an existing file."""
    file_name_with_ext = str(file_name) + ".txt"
    with open(file_name_with_ext, 'w') as file:
        file.write(file_content)


def append_file(file_name, file_content):
    """Appends content to a .txt file. Creates the file if it does not exist."""
    file_name_with_ext = str(file_name) + ".txt"
    with open(file_name_with_ext, 'a') as file:
        file.write(file_content)


def read_file(file_name):
    """Reads content from a .txt file and returns it."""
    file_name_with_ext = str(file_name) + ".txt"
    with open(file_name_with_ext, 'r') as file:
        content = file.read()
    return content
