from PIL import Image, ImageFilter
im =Image.open ('C:\\UC.jpeg')

#Crop Image
#box = (40, 40, 80, 80)
#cropped_im = im.crop(box)
#cropped_im.save('cropped_UC.jpeg')

#Rotate Image 90 degrees and 180 degrees
#im_rot_90 = im.rotate(90)
#im_rot_90.save('im_rot_90.jpeg')

#im_rot_180 = im.rotate(180)
#im_rot_180.save('im_rot_180.jpeg')

#Color Transformation
greyscale_im = im.convert('L')
greyscale_im.save('greyscale_im.jpeg')