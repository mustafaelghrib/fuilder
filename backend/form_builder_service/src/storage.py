from storages.backends.gcloud import GoogleCloudStorage


class StaticStorage(GoogleCloudStorage):
    location = 'static'


class MediaStorage(GoogleCloudStorage):
    location = 'media'
