# import shutil #type:ignore
import os #type:ignore 
import zipfile #type:ignore
import shutil
import traceback

sd = r"C:\Users\caw16\AppData\Local\FoundryVTT\Data\worlds"
an = "test"



def zip_files(world_sel:list[str]|str = "all", user:str = os.getlogin(), rel_path:str = r"/AppData/Local/FoundryVTT/Data/worlds") -> None:

    path:str = f"C:/Users/{user}{rel_path}/"
    worlds:list[str] = [i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))]
    worlds_to_zip: list[str] = []  
    if world_sel == "all":
        for world in worlds:
            worlds_to_zip.append(world)
            #zip up all the files here
    
    elif isinstance(world_sel, list):
        
        for world in worlds:
            if world in world_sel:
                worlds_to_zip.append(world)
                #zip up all the files here
    elif isinstance(world_sel, str): #type:ignore
        if world_sel in worlds:
            sel_world = worlds[worlds.index(world_sel)]
            worlds_to_zip.append(sel_world)
            #zip up all the files here
    else:
        print(f"{world_sel} is not a valid world name")
        
    paths:list[str] = [f"{path}{world}/" for world in worlds_to_zip]

    #zipping files
    
    i = 0
    for p in paths:
        print(p)
        try:
            shutil.make_archive(worlds_to_zip[i], 'zip', p)
        except Exception as e:
            print(f"Error zipping files: {e}")
            traceback.print_exc()
        i += 1
    return

    
if __name__ == "__main__":
    zip_files()