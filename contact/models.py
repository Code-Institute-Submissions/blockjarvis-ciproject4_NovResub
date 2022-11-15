from django.db import models


class Contact(models.Model):
    order = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    image_url = models.URLField(max_length=1024)
    image = models.ImageField()

    def __str__(self):
        return self.name
