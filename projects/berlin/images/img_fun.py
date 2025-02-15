"""
from - https://stackoverflow.com/questions/64113710/extracting-gps-coordinates-from-image-using-python
"""
from exif import Image

my_image = "./6654_take_off.jpg"

def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == "S" or ref =='W' :
        decimal_degrees = -decimal_degrees
    return decimal_degrees

def image_coordinates(image_path):

    with open(image_path, 'rb') as src:
        img = Image(src)
    if img.has_exif:
        try:
            img.gps_longitude
            coords = (decimal_coords(img.gps_latitude,
                      img.gps_latitude_ref),
                      decimal_coords(img.gps_longitude,
                      img.gps_longitude_ref))
        except AttributeError:
            print ('No Coordinates')
    else:
        print ('The Image has no EXIF information')
        
    return({"imageTakenTime":img.datetime_original, "geolocation_lat":coords[0],"geolocation_lng":coords[1]})

vals = image_coordinates(my_image)
print (my_image)
print (vals["geolocation_lng"], ",", vals["geolocation_lat"])
print (vals["imageTakenTime"])
