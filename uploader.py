import shutil
drive_path = r"G:\My Drive\backups" 

def move_file(file:str, path:str):
    """
    Moves a file to a specified destination path.

    Args:
        file (str): The path to the source file to be moved.
        path (str): The destination directory or file path where the file should be moved.

    Raises:
        FileNotFoundError: If the source file does not exist.
        PermissionError: If there are insufficient permissions to move the file.
        shutil.Error: If an error occurs during the move operation.
    """
    shutil.move(file, path)
    

if __name__ == "__main__":
    move_file("redo-hahaha.zip", drive_path)