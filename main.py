from PIL import Image

img = Image.open('Screenshot_4.png')

width, height = img.size

new_width = int(width * 0.5)
new_height = height

img = img.resize((new_width, new_height))

cropped_img = img.crop((0, 0, 10, 10))

img.save('new.png')
cropped_img.save('www.png')