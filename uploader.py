import shutil
drive_path = r"G:\My Drive\backups" 

def move_file(file:str, path:str):
    shutil.move(file, path)
    

if __name__ == "__main__":
    move_file("redo-hahaha.zip", drive_path)