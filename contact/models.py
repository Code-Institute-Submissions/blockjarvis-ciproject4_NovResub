from django.db import models


class Contact(models.Model):
    order = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, null=False, blank=False)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.order
