import os
import re
from PIL import Image

def save_files(files_list):
    if not os.path.exists(files_path):
        os.system(f"mkdir {files_path}")
    for file in files_list:
        file.name = file.name.replace(" ","_")
        save_path = f"{files_path}/{file.name}"
        pattern = re.compile(".pdf")
        match = re.search(pattern, save_path)
        if match:
            with open(save_path, mode='wb') as w:
                w.write(file.getvalue())
        else:
            im = Image.open(file)
            im.save(save_path)
    return True