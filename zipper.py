import zipfile #type:ignore
import os #type:ignore 


def zip_files(world_sel:list[str]|str = "all", user:str = os.getlogin(), rel_path:str = r"/AppData/Local/FoundryVTT/Data/worlds") -> None:

    path:str = f"C:/Users/{user}{rel_path}/"
    print(path)
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
    elif isinstance(world_sel, str):
        if world_sel in worlds:
            sel_world = worlds[worlds.index(world_sel)]
            worlds_to_zip.append(sel_world)
            #zip up all the files here
    else:
        print(f"{world_sel} is not a valid world name")
        
    print(worlds_to_zip)
        
        
        
    # with zipfile.ZipFile(f"{world}.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
    #     for root, _, files in os.walk(path):
    #         for file in files:
    #             file_path = os.path.join(root, file)
    #             arcname = os.path.relpath(file_path, start=path)
    #             zipf.write(file_path, arcname)
    
    
    
if __name__ == "__main__":
    zip_files()