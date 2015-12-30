import os
import shutil
from datetime import date

def content_data(f,path):
    #get year, month, date from file
    content_date = date.fromtimestamp(os.stat(path + os.sep + f).st_mtime)
    y,m,d = content_date.year, content_date.month, content_date.day
    if m < 10:
        m = '0'+ str(m)
    if d < 10:
        d = '0' + str(d)
    return y,m,d
def filter_function(x): return (x.count('.') == 1)

def rename_files(path):
#rename files in new directory
    files = os.listdir(path)
    for f in filter(filter_function,files):
            print f
            y,m,d = content_data(f,path)
            f_name, f_ext = f.split('.')
            f_new = "".join([f_name,'_',str(y),str(m),str(d),'.',f_ext])
            src = path + os.sep + f
            src_new = path + os.sep + f_new
            try:
                os.rename(src,src_new)
            except OSError as o:
                print f_new, "cannot be renamed"
                print o
                
def import_sony_pictures():
    # import from config file
    pic_path = 'C:\Users\Julia\Pictures'
    
    pic_dirs = os.listdir(pic_path)
    sony_dirs = [ x for x in pic_dirs if (x.endswith('2014') or x.endswith('2015'))]
    
    print sony_dirs
    
    for d in sony_dirs:
            day,m,y = d.split('.')
            #replace by os.path.join
            old_dir = "".join([pic_path,os.sep,d])
            new_dir_part = "".join([y,m,day])
            #replace by os.path.join        
            new_dir = "".join([pic_path,os.sep,new_dir_part,os.sep])
            print old_dir
            print new_dir
            if new_dir_part not in pic_dirs:
            #rename directory
                    os.rename(old_dir,new_dir)
                    rename_files(new_dir)
            else:
            #copy files
                    print new_dir, ' already exisits'
                    files = os.listdir(old_dir)
                    for f in filter(filter_function,files):
                            print f
                            y,m,d = content_data(f,old_dir)
                            f_name, f_ext = f.split('.')
                            f_new = "".join([f_name,'_',str(y),str(m),str(d),'.',f_ext])
                            src = old_dir + os.sep + f
                            src_new = old_dir + os.sep + f_new
                            try:
                                os.rename(src,src_new)
                                shutil.move(src_new,new_dir)
                            except OSError as o:
                                print f_new, "cannot be renamed"
                                print o
                            except shutil.Error:
                                print f, " already exists in ", new_dir 
        
if __name__ == "__main__":
    import_sony_pictures()
