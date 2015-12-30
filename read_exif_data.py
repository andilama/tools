import exifread
from datetime import datetime

f = open(r"/home/andreas/Bilder/Lago Maggiore/P1110643.JPG", 'rb')

#process  file with exifread without thumbnails
tags = exifread.process_file(f, details=False)

#relevant tags for processing
checktags = ['Image Make', 'Image Model', 'EXIF DateTimeDigitized',
             'EXIF DateTimeOriginal']
fileinfo = {}         

#datetime format
dt_format = "%Y:%m:%d %H:%M:%S"
try:
        for tag in checktags:
            fileinfo[tag] = tags[tag]
            
        exif_date = str(tags['EXIF DateTimeDigitized'])
        exif_dt = datetime.strptime(exif_date, dt_format)
        fileinfo['EXIF DateTimeDigitized'] = exif_dt
        
        exif_date = str(tags['EXIF DateTimeOriginal'])
        exif_dt = datetime.strptime(exif_date, dt_format)
        fileinfo['EXIF DateTimeOriginal'] = exif_dt
except KeyError:
    print("key not found")
except ValueError:
    print("Format not found")

for k,v in fileinfo.items():
    print(k,v)