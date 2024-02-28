from rembg import remove
from PIL import Image
input_path = 'scan.jpg'
output_path = 'newscan.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)