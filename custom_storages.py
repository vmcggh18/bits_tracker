from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# add class to deal with static files
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    
# add class to deal with media files
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
