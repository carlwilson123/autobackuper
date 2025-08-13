#region imports
import urllib.request
import os
import psutil
import time as t


# endregion

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





#region setup
url = "https://dl.google.com/drive-file-stream/GoogleDriveSetup.exe"
print("downloading drive for desktop, please add a drive for local...")
if not os.path.exists("GoogleDriveSetup.exe"): urllib.request.urlretrieve(url, "GoogleDriveSetup.exe")

print("running setup...")

os.startfile("GoogleDriveSetup.exe")

while is_program_running("GoogleDriveSetup.exe"):
    print(is_program_running("GoogleDriveSetup.exe"))
    t.sleep(1)

print("removing exe...")

os.remove("GoogleDriveSetup.exe")
#endregion


os.system("pip install -r requirements.txt")