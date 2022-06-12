import cloudinary
import cloudinary.uploader
from Models.video_response import *
import os
from repository import *

allowed_ext = ['mp4', 'mov', 'wmv', 'flv']

def upload_video(file, title, email) -> VideoResponse:
    fname = file.filename
    video_name = fname.split('.')[0]
    ext = fname.split('.')[1]
    if (ext not in allowed_ext):
        r = VideoResponse('500', 'Invalid format', '')
    else:
        cloud_name = os.environ['CLOUDINARY_CLOUD_NAME']
        api_key = os.environ['CLOUDINARY_API_KEY']
        api_secret = os.environ['CLOUDINARY_API_SECRET']
        try:
            cloudinary.config(cloud_name=cloud_name, api_key=api_key, api_secret=api_secret)
            upload_result = cloudinary.uploader.upload(file, resource_type='video')
            url = upload_result['url']
            r = VideoResponse('200', 'Uploaded', url)
        #     persist
            try:
                saveVideo(video_name, ext, url, title, email)
            except:
                r = VideoResponse('500', 'Error persisting', '')
        except:
            r = VideoResponse('500', 'Error while uploading', '')

    return r
