from django.db import models
import random
import os

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    new_filename = random.randit(1,39102938273)
    name,ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename=final_filename)

class ProductManager(models.Manager):
    def get_by_id(self,id):
        return self.get_queryset().filter(id=id)



class Product(models.Model):
    title = models.CharField(max_length = 120)
    description =models.TextField()
    price = models.DecimalField(max_digits = 10,decimal_places = 2,default = 344)
    image =models.ImageField(upload_to="products" ,null=True,blank = True)

    objects = ProductManager()

    def __str__(self):
        return self.title 
    
    def __unicode__(self):
        return self.title


