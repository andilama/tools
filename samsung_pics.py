import os
import shutil

path = r"C:\Users\Julia\Pictures\Samsung"
pic_path = r"C:\Users\Julia\Pictures"

pic_dirs = os.listdir(pic_path)
files = os.listdir(path)
counter = 0

for f in files:
    print(f)
    y,m,d = (f[:4],f[4:6],f[6:8])
    new_dir_part = "".join([y,m,d])
    new_dir = "".join([pic_path,os.sep,new_dir_part,os.sep])
    if new_dir_part not in pic_dirs:
        print(new_dir, " created")
        os.mkdir(new_dir)
        pic_dirs.append(new_dir_part)
    #else:
    #print new_dir, " exists already"
    src = path + "\\" + f
    try:
        shutil.move(src,new_dir)
        counter += 1
    except shutil.Error:
        print(f, " already exists in ", new_dir)
print(counter, " pictures copied")