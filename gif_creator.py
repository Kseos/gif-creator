from PIL import Image
import imageio.v3 as iio
from pathlib import Path

filenames = ['images/1.jpg', 'images/2.jpg']
images = []

first_image = Image.open(filenames[0])
first_size = first_image.size

for file in filenames:
    img = Image.open(file)
    img_resized = img.resize(first_size, Image.LANCZOS)
    images.append(img_resized)
 
download_folder = Path.home()/'Downloads'
output_path = str(download_folder/'created_gif.gif')

iio.imwrite(output_path, images, duration = 500, loop = 0)

print(f'GIF was downloaded in: {output_path}')
    

