#!/usr/bin/python3
print("loading 15%")
import os,sys,shutil
from tkinter import filedialog
import tkinter as tk
import logging
print("loading 50%")
root=tk.Tk()
root.withdraw()
print("loading 65%")
logging.basicConfig(filename=".file_organiser.log",level=logging.DEBUG,format="%(asctime)s - %(message)s")
print("loading 75%")
DIRECTORIES = {
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif", ".psd"], 
    "Video": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"], 
    "Compressed": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"], 
    "Music": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"], 
    "Documents": [".txt", ".in", ".out",".pdf",".xml",".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt"
    ,".html5", ".html", ".htm", ".xhtml", "pptx",".sh",".djvu",".ppsx",".c",".cpp",".py",".sh",".o",".css",".js"], 
    "Programs": [".exe",".vbs",".bat",".msi"], 
    "Torrents": [".torrent"],
    "Shortcuts": [".lnk"],
    "Linux Installers": ['.deb','.appimage'],
    "Other": [".crx"],
    
}
print("loading 100%")
dir=""
if(len(sys.argv[:])<2):
    print("opening folder chooser...")
    dir=filedialog.askdirectory()
else:
    dir=''.join(sys.argv[1:])
os.chdir('/')
os.chdir(dir)
dirs=[]
filenames=[]
for root,dirs,filenames in os.walk('.'):
    break
#dirs=os.listdir()
print("in dir:",os.getcwd())
logging.debug("in dir:"+os.getcwd())

for i in DIRECTORIES.keys():
    if(i.lower() not in dirs):
        try:
            os.mkdir(i)
            print(i + " CREATED!")
        except Exception as err:
            logging.debug(err)
            continue
    
for current in filenames:
    filename,fileext=os.path.splitext(current)
    f=0
    for folder,ext in DIRECTORIES.items():
        if(fileext.lower() in ext):
            f=1
            try:
                folder=os.path.join('.',folder)
                shutil.move(current,folder)
                print("moving ",current," to directory ",folder)
                logging.debug("moving "+ current+" to directory "+folder)
            #except (shutil.Error , FileExistsError ) as err:
            #   print("\ncould not move ",current," to directory ",folder)
            #   logging.debug("could not move "+current+" to directory "+folder)
            #   logging.debug(err)
            except Exception as err: 
                print("\ncould not move ",current," to directory ",folder)
                logging.debug("could not move "+current+" to directory "+folder)
                logging.debug(err)
                
                #break
    if(f==0):
        folder="Other"
        try:
            folder=os.path.join('.',folder)
            shutil.move(current,folder)
            print("moving ",current," to directory ",folder)
            logging.debug("moving "+ current+" to directory "+folder)
        except (shutil.Error , FileExistsError) as err:
            print("\ncould not move ",current," to directory ",folder)
            logging.debug("could not move "+current+" to directory "+folder)
            logging.debug(err)
        except Exception as err: 
            print("\ncould not move ",current," to directory ",folder)
            logging.debug("could not move "+current+" to directory "+folder)
            logging.debug(err)
            #break
print("\n\n*********\n\nDONE ORGANISING FILE(s)\n*******\n\n")
logging.debug("END!\n\n")
input("Press Enter to exit!");
    


    

