from mongoengine import *

class Count(Document):
    amount = IntField()
    time = DateTimeField()