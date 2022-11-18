import shutil
import os

path = 'C:/Program Files (x86)/Steam/steamapps/workshop/content/529340'

def make_new_folder(folder_name, parent_folder):
    path = os.path.join(parent_folder, folder_name)
    try: 
        mode = 0o777
        os.mkdir(path, mode) 
    except OSError as error: 
        print(error)

current_folder = path
list_dir = os.listdir(path)
list_dir.remove('.git')
list_dir.remove('.gitattributes')
list_dir.remove('merge.py')
content_list = {}
for index, val in enumerate(list_dir):
    path = os.path.join(current_folder, val)
    content_list[ list_dir[index] ] = os.listdir(path)
merge_folder = "merge_folder"
merge_folder_path = os.path.join(current_folder, merge_folder) 
make_new_folder(merge_folder, current_folder)
for sub_dir in content_list:
    for contents in content_list[sub_dir]:
        path_to_content = sub_dir + "/" + contents  
        dir_to_move = os.path.join(current_folder, path_to_content )
        shutil.move(dir_to_move, merge_folder_path)