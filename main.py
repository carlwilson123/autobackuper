from zipper import zip_files #type: ignore
from uploader import move_file #type: ignore
import time as t
import psutil
import sys
#this handles mainly launching the foundry exe and making sure that when it clothese 

#region functions
def is_program_running(program_name:str ) -> bool:
    """
    Checks if a program with the specified name is currently running.
    Args:
        program_name (str): The name of the program to check.
    Returns:
        bool: True if the program is running, False otherwise.
    """

    for proc in psutil.process_iter(['name']) : #type:ignore put here because mypy is not able to infer the type of proc.info since it is a "generator" not a Generator
        if proc.info['name'] == program_name:
            return True
    return False
#endregion



### do not run if your pc is on the lower end, python might tax your system too much


while is_program_running("Foundry Virtual Tabletop.exe"):
    print("FoundryVTT is still running...")
    t.sleep(5)


args_in:list[str] = sys.argv[1:]

if len(args_in) > 1:
    zip_paths = zip_files()
else:
    args = args_in[0].split(",")
    zip_paths = zip_files(world_sel=args)


upload_path = r"G:\My Drive\backups"



for zip in zip_paths:
    move_file(zip, upload_path)
