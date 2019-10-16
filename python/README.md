# Lab7 assignment
Below is my 3 examples I used with my python plugin Pillow.

##Installation

To install Pillow you run the following command:
```pip install pillow```

#Find your picture
You can pick any jpeg photo on the google images and save it directly to your hard drive. You will need to call the photo, to do so use the following command when in python:

```python
from PIL import Image, ImageFilter
im =Image.open ('The path to image.jpeg')
```

#Crop image
To crop your desired image you will want to run the following command, different images have different demension:

```python
box = (40, 40, 80, 80)
cropped_im = im.crop(box)
cropped_im.save('cropped_im.jpeg')
```

#Rotate image 90 & 180 degrees
To rotate your image 90 and 180 degrees you will run the following command:

```python
im_rot_90 = im.rotate(90)
im_rot_90.save('im_rot_90.jpeg')

im_rot_180 = im.rotate(180)
im_rot_180.save('im_rot_180.jpeg')
```

#Turn your photo grey
To put a grey color scheme on your photo you will want to run the following command:

```python
greyscale_im = im.convert('L')
greyscale_im.save('greyscale_im.jpeg')
```

Hope these created some neat variations of your original photo!