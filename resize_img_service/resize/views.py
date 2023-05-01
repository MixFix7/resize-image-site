from django.shortcuts import render
from resize.resize import create_image
from io import BytesIO
from PIL import Image
import os


def home(request):
    return render(request, 'index.html')

def result(request):
    if request.method == 'POST':
        image_get = request.FILES.get('ent')
        get_height = int(request.POST.get('height'))
        get_width = int(request.POST.get('width'))
        print(get_width)

        image1 = image_get.read()
        image = Image.open(BytesIO(image1))
        width, height = image.size


        new_height = int(height * get_width / width)
        new_width = get_width
        print(new_width, new_height)

        resized_img = image.resize((new_width, new_height))

        cropped_img = resized_img.crop((0, 0, new_width, new_height))

        image.save("static/images/img.png")


        return render(request, 'index.html', {'img': image})
    else:
        return render(request, 'index.html')