from django.db import models
from django.urls import reverse
import random
import os
from django.db.models import Q
from django.conf import settings
User = settings.AUTH_USER_MODEL

CATEGORY1_CHOICES = (
    ('men', 'Men'),
    ('houselinen', 'House-Linen'),
    ('ladies', 'Ladies'),
    ('polishing','Polishing'),
    ('homecleaningservices','Home-Cleaning-Services'),

)

CATEGORY2_CHOICES = (
    ('washsteampress', 'Wash-Steam-Press'),
    ('dryclean', 'Dry-Clean'),
    ('steampress', 'Steam-Press'),
    ('misc','Misc'),
)

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) | 
                  Q(description__icontains=query) |
                  Q(price__icontains=query) |
                  Q(tag__title__icontains=query)
                  )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)

class Product(models.Model):
    user            = models.ForeignKey(User,on_delete=models.CASCADE)
    title           = models.CharField(max_length=120)
    description     = models.CharField(max_length=120, null=True, blank=True)
    image           = models.FileField(upload_to=upload_image_path, null=True, blank=True)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    category1       = models.CharField(max_length=120, default=CATEGORY1_CHOICES[0][0], choices=CATEGORY1_CHOICES)
    category2       = models.CharField(max_length=120, default=CATEGORY2_CHOICES[0][0], choices=CATEGORY2_CHOICES)
    price           = models.FloatField()
    created_timestamp = models.DateTimeField(auto_now=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    
    objects = ProductManager()

    def get_absolute_url(self):
        return reverse("product:details")

    def __str__(self):
        return str(self.id)+"-"+self.title

    def __unicode__(self):
        return self.title

    @property
    def name(self):
        return self.title

    class Meta:
        db_table = "product"
        ordering = ['-updated_timestamp']

    