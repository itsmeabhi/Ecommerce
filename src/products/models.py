# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import random
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db.models import Q

# Create your models here.

'''
Below two functions are used to store the imaged with the random file name in the media storage. 
'''


def get_extension(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext


def get_newfilename(instance, filename):
    new_filename = random.randint(1, 2232323)
    name, ext = get_extension(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


'''
Custom manager for for relative simple query functions core object query :)
'''


class ProductManager(models.Manager):
    def get_by_id(self, pk):
        qs = self.get_queryset().filter(pk=pk)
        if len(qs) == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().filter(Q(title__icontains=query)
                                          | Q(description__icontains=query)).distinct()


class Product(models.Model):  # PRODUCT MODEL
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField(null=True)
    image = models.ImageField(upload_to=get_newfilename, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)

    objects = ProductManager()

    # Used for reverse URL as products/{slug} is hardcoded.
    def get_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


'''
As soon as Model load and we are adding the product model object we need to slugify that object so pre-save method is used.
'''
@receiver(pre_save, sender=Product)
def my_callback(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
