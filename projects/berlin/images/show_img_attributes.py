"""
show exif attributes on an image
from - https://exif.readthedocs.io/en/latest/usage.html
"""

from exif import Image
img = Image("./6654_take_off.jpg")
image_attributes = dir(img)
print(image_attributes)

































# for attribute in image_attributes:
	# print(attribute)



print ()
print(img.gps_longitude_ref, img.gps_longitude, img.gps_latitude_ref, img.gps_latitude)
