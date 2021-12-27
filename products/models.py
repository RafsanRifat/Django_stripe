from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(default=0, blank=True, null=True)  # cents
    file = models.FileField(upload_to="product_files/", blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)