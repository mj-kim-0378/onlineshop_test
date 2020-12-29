from storages.backends.s3boto3 import S3Boto3Storage

class MedeiaStorage(S3Boto3Storage):
    location = ""
    bucket_name = 'onlineshop1-media'
    region_name = 'ap-northeease-2'
    custom_domain = f"s3.{region_name}.amazonaws.com/{bucket_name}"
    file_overwrite=False