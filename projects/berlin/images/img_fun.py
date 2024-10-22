"""
from - https://stackoverflow.com/questions/64113710/extracting-gps-coordinates-from-image-using-python
"""
from exif import Image

my_image = "./6780_sunday_cake.jpg"

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
print (vals["imageTakenTime"])
print (vals["geolocation_lng"], ",", vals["geolocation_lat"])


# from exif import Image
# img = Image("./cake.jpg")
# print(img.gps_longitude_ref, img.gps_longitude, img.gps_latitude_ref, img.gps_latitude)
# print(img._exif_ifd_pointer)
# print(img._gps_ifd_pointer)
# image_attributes = dir(img)
# print(image_attributes)
"""
[
    '<unknown EXIF tag 316>', '<unknown EXIF tag 322>', '<unknown EXIF tag 323>', '<unknown EXIF tag 42080>', 
    '_exif_ifd_pointer', '_gps_ifd_pointer', '_segments', 
    'aperture_value', 'brightness_value', 'color_space', 
    'components_configuration', 'datetime', 'datetime_digitized', 'datetime_original', 
    'delete', 'delete_all', 'exif_version', 'exposure_bias_value', 'exposure_mode', 
    'exposure_program', 'exposure_time', 'f_number', 'flash', 'flashpix_version', 
    'focal_length', 'focal_length_in_35mm_film', 'get', 'get_all', 'get_file', 
    'get_thumbnail', 'gps_altitude', 'gps_altitude_ref', 'gps_datestamp', 
    'gps_dest_bearing', 'gps_dest_bearing_ref', 'gps_horizontal_positioning_error', 
    'gps_img_direction', 'gps_img_direction_ref', 'gps_latitude', 'gps_latitude_ref', 
    'gps_longitude', 'gps_longitude_ref', 'gps_speed', 'gps_speed_ref', 'gps_timestamp', 
    'has_exif', 'lens_make', 'lens_model', 'lens_specification', 'list_all', 'make', 
    'maker_note', 'metering_mode', 'model', 'offset_time', 'offset_time_digitized', 
    'offset_time_original', 'orientation', 'photographic_sensitivity', 'pixel_x_dimension', 
    'pixel_y_dimension', 'resolution_unit', 'scene_capture_type', 'scene_type', 
    'sensing_method', 'shutter_speed_value', 'software', 'subject_area', 
    'subsec_time_digitized', 'subsec_time_original', 'white_balance', 'x_resolution', 
    'y_and_c_positioning', 'y_resolution']
"""

# print(img.focal_length)




"""
from - https://geojson.org
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [125.6, 10.1]
  },
  "properties": {
    "name": "Dinagat Islands"
  }
}
"""