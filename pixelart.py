from PIL import Image
import numpy as np

while True:
    path = input("Enter the path of the image to convert: ")
    try:
        img = Image.open(path)
        break
    except FileNotFoundError:
        print("Sorry, I couldn't find that file.")

width, height = img.size
pixel_width = 20
pixel_height = int(height*pixel_width/width)

pixels_per_grid_w = int(width/pixel_width)
pixels_per_grid_h = int(height/pixel_height)

avg = pixels_per_grid_h * pixels_per_grid_w

horizontal = []

for ii in range(pixel_height):
    picture_array = []
    for jj in range(pixel_width):
        # get all rgb values in an pixel_w x pixel_h grid
        rgb_list = []
        for i in range(ii*pixels_per_grid_h, (ii+1)*pixels_per_grid_h):
            for j in range(jj*pixels_per_grid_w, (jj+1)*pixels_per_grid_w):
                r, g, b = img.getpixel((j,i))
                rgb_list.append([r,g,b])

        # averages all rgb values 
        r_total, g_total, b_total = 0, 0, 0
        for rgb in rgb_list:
            r_total += rgb[0]
            g_total += rgb[1]
            b_total += rgb[2]
        picture_array.append((int(r_total/avg),int(g_total/avg),int(b_total/avg)))

    horizontal.append(picture_array)

# scales picture up significantly
scale = 20
img_array = []
for list_ in horizontal:
    new_list = []
    for item in list_:
        for i in range(20):
            new_list.append(item)
    
    for i in range(scale):
        img_array.append(new_list)

# converts horizontal into an array and then into a picture
array = np.array(img_array, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.save('new.png')