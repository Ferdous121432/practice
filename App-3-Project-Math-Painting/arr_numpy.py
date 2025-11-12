import numpy as np
from PIL import Image


data = np.zeros((3, 4, 3), dtype=np.uint8)
data[:] = [255, 0, 0]  # Red color
data[0:1, 3:4] = [0, 255, 0]  # Green color
data[1:2, 3:4] = [0, 0, 255]  # Blue color

img = Image.fromarray(data, 'RGB')
img.save('red_image.png')
print(data)
