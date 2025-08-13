#region imports
import urllib.request
import os
import psutil
import time as t
from typing import Generator

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

    for proc in psutil.process_iter(['name']) :
        if proc.info['name'] == program_name:1
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