# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import random
from django.db import models

# Create your models here.


def get_extension(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext


def get_newfilename(instance, filename):
    new_filename = random.randint(1, 2232323)
    name, ext = get_extension(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField(null=True)
    image = models.FileField(upload_to=get_newfilename, null=True, blank=True)

    def __str__(self):
        return self.title

