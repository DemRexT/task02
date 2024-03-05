from collections import namedtuple
import os
import sys

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_files_info(path):
    files_info = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        parent_dir = os.path.basename(os.path.dirname(full_path))
        is_dir = os.path.isdir(full_path)
        
        if is_dir:
            name = item
            extension = None
        else:
            name, extension = os.path.splitext(item)
        
        files_info.append(FileInfo(name=name, extension=extension, is_directory=is_dir, parent_directory=parent_dir))

    return files_info


if '__name__ '== "__main__": 
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    files_info = get_files_info(directory_path)

    for file_info in files_info:
        print(file_info)
    assert get_files_info("test_empty_directory") == []

    assert os.system('python script.py wrong_path') == 1

     
