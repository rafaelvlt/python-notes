import shutil, os, os.path
from pathlib import Path

def copySelector(folder, newFolder, extension):
    '''
    folder = directory you want to copy the ftree
    newFolder = creates the destination where you send new copys
    extension = extension you want to copy, don't need the dot in the beginning
    '''
    #checks if the user ignored the docstring and put the dot anyway
    if extension[0] != ".":
     extension = '.' + extension
    else:
       None
    #gets the absolute path of the folders and checks if the destination exist
    folder = Path(Path.cwd() / folder)
    newFolder = Path(Path.cwd() / newFolder)
    print(newFolder)
    if newFolder.is_dir() == False:
        os.makedirs(newFolder)
    else:
        None
    #walks through de folder copying the contents specified
    for foldername, subfolders, filenames in os.walk(folder):
        print("Copying the contents of folder: " + foldername)
        #copy each file to the newfolder
        foldername = Path(Path.cwd() / foldername)
        for filename in filenames:
            if filename[-4:] == '.txt':
                shutil.copy(foldername / filename, newFolder / filename)
            else:
                None
    print("Copied!")

foldert = input("folder name ")
destinyt = input("destination ")
extensiont = input("extension ")
copySelector(foldert, destinyt, extensiont)
