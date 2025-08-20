# Autobackuper

A utility for automating backups using Python.

## Features
- Automated backup process
- Google API integration

## Requirements
- Python 3.7+
- See `requirements.txt`

## Setup
in powershell when in directory run

```powershell
.\runsetup
```

## License
MIT


## code 

### Zipper.py

This code defines a function called zip_files that automates the backup of FoundryVTT world directories by compressing them into zip files. The function is designed to be flexible: you can specify which worlds to back up by passing a list of world names, a single world name, or the string "all" to back up every world found in the target directory. The function also allows you to specify the user and the relative path to the worlds directory, defaulting to the current OS user and a standard FoundryVTT path.

The function first constructs the full path to the worlds directory and lists all subdirectories, assuming each represents a world. It then determines which worlds to zip based on the world_sel argument. If "all" is specified, it selects every world; if a list is provided, it matches only those names; if a single string is given, it checks for that world. If the selection is invalid, it prints an error message.

For each selected world, the function builds the full path and uses shutil.make_archive to create a zip file in a "backups" directory, naming each archive after the world. It prints the path being zipped for visibility and collects the paths to the created zip files in a list. If any error occurs during zipping, it prints the error and a stack trace for debugging. The function returns a list of the zip file paths it created.

When the script is run directly, it calls zip_files() with default arguments, attempting to back up all worlds for the current user. This makes it easy to use for regular backups or migration tasks. The code is robust, with error handling and clear output, but assumes the existence of a "backups" directory and that the user has permission to read and write in the relevant locations.

### setup.py
This script automates the installation of Google Drive for Desktop and Python dependencies for this project. It starts by importing modules for downloading files, interacting with the operating system, monitoring running processes, and handling time delays.

The function is_program_running checks if a process with a given name is currently running. It uses psutil.process_iter to iterate over all running processes and returns True if it finds a match, otherwise False.

In the setup section, the script defines the URL for the Google Drive installer. If the installer file does not already exist locally, it downloads it using urllib.request.urlretrieve. It then launches the installer with os.startfile and enters a loop, repeatedly checking if the installer process is still running. During this time, it prints the running status and waits one second between checks.

Once the installer finishes, the script deletes the installer file to clean up. Finally, it runs pip install -r requirements.txt to install any Python packages listed in the requirements file, ensuring the environment is ready for the project. This approach streamlines both the setup of cloud storage and Python dependencies, making it easier to prepare a new system for development or deployment.