import json
import os

def load_data(File=None,list=None):
    if os.path.exists(File):
        with open(File,'r') as file:
            content=file.read().strip()
            list=json.loads(content)if content else []
            return list

def save_file(File=None,list=None):
    with open(File,"w") as file:
        json.dump(list,file,indent=2)


def destroy_win(win=None):
    win.destroy()