import os
import shutil
from datetime import date

path = "C:\Users\Julia\Pictures\Sony"
pic_path = "C:\Users\Julia\Pictures"

pic_dirs = os.listdir(pic_path)
files = os.listdir(path)
counter = 0
def filter_function(x): return not x.endswith('THM')

def content_data(f):
    #get year, month, date from file
    content_date = date.fromtimestamp(os.stat(path + os.sep + f).st_mtime)
    y,m,d = content_date.year, content_date.month, content_date.day
    if m < 10:
        m = '0'+ str(m)
    if d < 10:
        d = '0' + str(d)
    return y,m,d

for f in filter(filter_function, files):
    y,m,d = content_data(f)
    #construct directory
    new_dir_part = "".join([str(y),str(m),str(d)])
    new_dir = "".join([pic_path,os.sep,new_dir_part,os.sep])
    if new_dir_part not in pic_dirs:
        os.mkdir(new_dir)
        print new_dir, " created"
        pic_dirs.append(new_dir_part)
    #copy file
    f_name, f_ext = f.split('.')
    f_new = "".join([f_name,'_',str(y),str(m),str(d),'.',f_ext])
    src = path + os.sep + f
    src_new = path + os.sep + f_new
    try:
        os.rename(src,src_new)
        shutil.move(src_new,new_dir)
        counter += 1
    except OSError as o:
        print f_new, "cannot be renamed"
        print o
    except shutil.Error:
        print f_new, " already exists in ", new_dir     
print counter, " pictures copied"
