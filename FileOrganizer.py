import os
import shutil
import logging

CATEGORIES = { #Categories can be expanded as you desire
    
    "Images" : [".jpeg",".png",".jpg",".gif"],
    "Documents" : [".pdf",".txt",".docx"],
    "Videos" : [".mp4",".avi",".mov"],
    "Music" : [".mp3",".wav"],
  
  }

#This function will be responsible to record all the actions caused by the programm.
#Useful in case you lose track of a file
logging.basicConfig(
    filename=os.path.join(os.path.dirname(__file__), "organizer.log"), #File where the log will be saved
    level=logging.INFO, #Level of info messages being recorded
    format="%(asctime)s - %(message)s"
    )


def FileOrganizer(folder_path, dry_run=False):
    """
    Organizes files in the folder_path (and subfolders recursively) 
    according to their extension categories.
    """
    for root,dirs,files in os.walk(folder_path):
        # os.walk goes through all subfolders automatically
        for file in files:   
            file_ext=os.path.splitext(file)[1].lower() #This line of code is responsible for getting the extension of the file
            moved=False
            for category, extensions in CATEGORIES.items():
                if file_ext in extensions:
                        # folder_path = os.path.join(file_path,category) #This line of code is responsible for connecting the extension of the file to the path of the folder the file is going into
                        # os.makedirs(folder_path, exist_ok=True)

                        # source_path = os.path.join(file_path,file) #This line of code is responsible for joining the path of the file to the file itself, making it easier to spot the source of the file
                    destination_folder= os.path.join(folder_path,category) #This line of code is responsible for joining the folder path to the file, making it be stored on the destination folder

                        # shutil.move(source_path, destination_path)
                        # print(f"Moved {file} to {category}") #debug
                    moved = True
                    break
            
            if not moved:  # only if no category matched
                        # folder_path = os.path.join(file_path, "Misc")
                        # os.makedirs(folder_path, exist_ok=True)
                        # source_path = os.path.join(file_path, file)
                    destination_folder = os.path.join(folder_path, "Misc")
                        # shutil.move(source_path, destination_path)
                        # print(f"Moved {file} to Misc")

                
                #Ensures the destination folder exists
            if not dry_run:
                   
                os.makedirs(destination_folder, exist_ok=True)

                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)     

                # Move the file (or simulate if dry_run=True)
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file)
            
            if dry_run:
                 logging.info(f"[DRY-RUN] Would move {source_path} to {destination_path}")
                 print(f"[DRY-RUN] Would move {source_path} -> {destination_path}")
            else:
                 shutil.move(source_path, destination_path)
                 logging.info(f"Moved {source_path} -> {destination_path}")
                 print(f"Moved {source_path} -> {destination_path}")

                
            

def FileItemsLister(filepath):
    
    print(f"Checking directory: {filepath}")  # debug
    files = os.listdir(filepath)
    print(f"Found {len(files)} items")        # debug
    return files

def main():
    folder= r"FolderNameHere"
    # files=FileItemsLister(folder) #<- uncomment if you want to check the files in the folder
    # Set dry_run=True to simulate without moving
    FileOrganizer(folder,dry_run=True)
    
if __name__ == "__main__":
    main()