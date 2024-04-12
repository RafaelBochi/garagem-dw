import uuid
from django.db import models

def upload_image_fomater(instance, filename):
    return f"{str(uuid.uuid4())}-{filename}"

class CarPic(models.Model):
    image = models.ImageField(upload_to=upload_image_fomater, blank=True, null=True)