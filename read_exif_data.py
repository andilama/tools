import os
import exifread
from datetime import datetime

f = open(r"C:\Users\Julia\Pictures\20140106\DSC05572.JPG", 'rb')

tags = exifread.process_file(f)

exif_date = str(tags['EXIF DateTimeDigitized'])

dt_format = "%Y:%m:%d %H:%M:%S"
exif_dt = datetime(exif_date, dt_format)
