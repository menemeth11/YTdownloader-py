from rembg import remove
from PIL import Image

input_path = 'C:\Users\szymo\Desktop\downloader\YTdownloader-py\mug1.jpg'
output_path = "newmug1.png"

input= Image.open(input_path)
output=remove(input_path)
output.save(output_path)