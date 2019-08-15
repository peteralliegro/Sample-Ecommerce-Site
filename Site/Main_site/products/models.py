from django.db import models
from django.db.models.signals import pre_save
import os, random
from .utils import unique_slug_generator


class ProductManager(models.Manager):
    def get_by_id(self, id):
        return self.get_queryset().filter(id=id)

   
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 9000000)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
        )

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=99.99)
    image = models.ImageField(upload_to=upload_image_path, null=False, blank=False)
    slug = models.SlugField(blank=True, default="", unique=True, editable=False)
    qauntity = models.IntegerField(blank=False, default=1)
    height = models.IntegerField(blank=True, default=1)
    length = models.IntegerField(blank=True, default=1)

    objects = ProductManager()

    def get_url(self):
        return"/products/{slug}/".format(slug=self.slug)

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
# Create your models here.
