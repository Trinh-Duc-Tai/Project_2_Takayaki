from mongoengine import *

class Video(Document): #kethua document
    title = StringField()
    views = IntField()
    likes = IntField()
    dislikes = IntField()
    youtube_id = StringField()
    link = StringField()
    time = DateTimeField()
    download_type = StringField()