from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

# Create your models here.
from products.models import Product


class Tag(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(blank=True, null=True)
    product = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Tag)
def my_callback(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)