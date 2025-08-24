# import shutil #type:ignore
import os #type:ignore 
import zipfile #type:ignore
import shutil
import traceback
from win32com.shell import shell, shellcon
import sys
import pyuac
import time as t



# def get_paths(world_sel:list[str]|str = "all", user:str = os.getlogin(), rel_path:str = r"/AppData/Local/FoundryVTT/Data/worlds") -> list[str]:
#     path:str = f"C:/Users/{user}{rel_path}/"
#     worlds:list[str] = [i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))]
#     worlds_to_zip: list[str] = []  
#     if world_sel == "all":
#         for world in worlds:
#             worlds_to_zip.append(world)
#             #zip up all the files here
    
#     elif isinstance(world_sel, list):
        
#         for world in worlds:
#             if world in world_sel:
#                 worlds_to_zip.append(world)
#                 #zip up all the files here
#     elif isinstance(world_sel, str): #type:ignore
#         if world_sel in worlds:
#             sel_world = worlds[worlds.index(world_sel)]
#             worlds_to_zip.append(sel_world)
#             #zip up all the files here
#     else:
#         print(f"{world_sel} is not a valid world name")
        
#     paths:list[str] = [f"{path}{world}/" for world in worlds_to_zip]
    
#     return paths, worlds_to_zip





def zip_files(paths: list[str], worlds_to_zip: list[str]) -> list[str]:
    #zipping files
    
    i = 0
    zip_refs:list[str] = []
    
    for p in paths:
        print(p)
        try:
            zip_ref = f"backups/{worlds_to_zip[i]}"
            zip_refs.append(zip_ref)
            shutil.make_archive(zip_ref, 'zip', p) 
        except Exception as e:
            print(f"Error zipping files: {e}")
            traceback.print_exc()
        i += 1
    return zip_refs





if __name__ == "__main__":
    # zip_files()
    # request_admin_privileges()
    target = r"backups"
    os.makedirs(target, exist_ok=True)
    shutil.copy(r"C:\Users\caw16\AppData\Local\FoundryVTT\Data\worlds\redo-hahaha\packs\mass-edit-presets-main\000017.log", target)
    for root,dirs,files in os.walk(r"C:\Users\caw16\AppData\Local\FoundryVTT\Data\worlds\redo-hahaha"):
        # print(root,dirs,files)
        
        if dirs == []:
            for file in files:
                # print(root,file)
                # print(os.path.exists(os.path.join(root, file)))
                path = os.path.join(root, file)
                
                org_pers_list = path.split("\\")
                
                org_pers_list = org_pers_list[org_pers_list.index("redo-hahaha") : ]

                
                
                backup_path = os.path.join(target, ("\\").join(org_pers_list))
                print(os.path.exists(os.path.dirname(backup_path)))
                if not os.path.exists(os.path.dirname(backup_path)):
                    os.makedirs(os.path.dirname(backup_path))

        stop = True

        target_folder = r"backups\redo-hahaha"

    
    shutil.make_archive(target_folder, "zip", target_folder)
    t.sleep(5)
    shutil.rmtree(target_folder)
    # a, b = get_paths()
    
    # zip_files(a, b)