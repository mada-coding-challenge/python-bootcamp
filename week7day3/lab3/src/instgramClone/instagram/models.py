from django.core.exceptions import ValidationError
from django.db import models
import os


def validate_image_extension(value):
    extension = os.path.splitext(value.name)[1].lower()

    if extension not in [".jpg", ".jpeg", ".png"]:
        raise ValidationError(
            "Only JPG, JPEG, and PNG images are allowed."
        )


class Post(models.Model):
    username = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to="posts/",
        validators=[validate_image_extension],
    )
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.username