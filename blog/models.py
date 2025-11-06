from django.db import models
import random
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=True)


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(max_length=100, null=True)
    img_url = models.CharField(max_length=50, null=True)
    slug = models.SlugField(unique=True, null=True)
    rating = models.IntegerField(default=0, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.rating:
            self.rating = random.randint(3, 5)

        if not self.price:
            self.price = random.randint(20, 50)

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title