from PIL import Image
from datetime import datetime
from dotenv import dotenv_values
import os
import shutil
import time

# get environment variables
config = dotenv_values(".env") 
fotos_dir = config['FOTOS_DIRECTORY']
script_dir = config['HOME_DIRECTORY']
output_dir = config['OUTPUT_DIRECTORY']

#change to script home directory
os.chdir(script_dir)


# imagename = "/home/nicolas/Desktop/pixel3-fotos/fotos/PXL_20220422_134508310.jpg"
images_list = os.listdir(fotos_dir)

for i in images_list:

    try:

    
        image = Image.open(f"{fotos_dir}/{i}")
        metadata = image.getexif()
        img_date = metadata.get(306)
        py_date = datetime.strptime(img_date, '%Y:%m:%d %H:%M:%S')
        year = str(py_date.year)
        month = str(py_date.month)

        foto_dir = f"{fotos_dir}/{i}"
        year_dir = f"{output_dir}/{str(year)}"
        month_dir = f"{output_dir}/{str(year)}/{str(month)}"

        if not os.path.isdir(year_dir):
            os.mkdir(year_dir)
        
        if not os.path.isdir(month_dir):
                os.mkdir(month_dir)

        shutil.move(foto_dir, month_dir)
    
    except:

        c_time = os.path.getmtime(f"{fotos_dir}/{i}")
        timex = time.ctime(c_time)

        movie_date = datetime.strptime(timex, '%a %b %d %H:%M:%S %Y')
        year = str(movie_date.year)
        month = str(movie_date.month)

        foto_dir = f"{fotos_dir}/{i}"
        year_dir = f"{output_dir}/{str(year)}"
        month_dir = f"{output_dir}/{str(year)}/{str(month)}"

        if not os.path.isdir(year_dir):
            os.mkdir(year_dir)
        
        if not os.path.isdir(month_dir):
                os.mkdir(month_dir)

        shutil.move(foto_dir, month_dir)

