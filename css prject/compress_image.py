import PIL.Image as Image
from io import BytesIO
import os
def compress_image(image_path, quality=85):
  image_path = os.path.join(os.getcwd(), image_path)
  with Image.open(image_path) as img:
    if img.format != 'JPEG':
      img = img.convert('RGB')

    output = BytesIO()

    img.save(output, format='JPEG', quality=quality)

    return output.getvalue()

compressed_data = compress_image('./imgs/Final.png', quality=75)
with open('compressed_image.jpg', 'wb') as f:
  f.write(compressed_data)