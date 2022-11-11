import os
from PIL import Image
from flask import current_app, url_for

def upload_photo(pic_upload,username):

    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    storage_filename = str(username) + '.' +ext_type
    
    filepath = os.path.join(current_app.root_path, 'static.profile_pics', storage_filename)
    output_size = (400, 400)
    userphoto = Image.open(pic_upload)
    userphoto.thumbnail(output_size)
    userphoto.save(filepath)








    return storage_filename
