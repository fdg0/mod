import shutil
import os

# Source path 
src = 'C:/Program Files (x86)/Steam/steamapps/workshop/content/529340/'
 
# Destination path 
dest = 'C:/Program Files (x86)/Steam/steamapps/workshop/content/529340/multiplayer_synchronized/'

list_dir = os.listdir(src)
list_dir.remove('.git')
list_dir.remove('.gitattributes')
list_dir.remove('merge.py')
list_dir.remove('multiplayer_synchronized')
list_dir.remove('.gitignore')

for sub_dir in list_dir:
    sub_dir_2 = src+sub_dir
    try: 
        shutil.copytree(sub_dir_2, dest,dirs_exist_ok=True)
    except OSError as error: 
        print(error)
    


            