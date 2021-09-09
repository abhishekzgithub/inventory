from django.db import models
from product.models import Product
from django.conf import settings
from django.db.models.signals import pre_save, post_save, m2m_changed, pre_delete, post_delete
from decimal import Decimal
from django.db.models import Count

User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)
    created_timestamp = models.DateTimeField(auto_now=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "cart"

    def __str__(self):
        return str(self.id)
    
    @property
    def cart_subtotal(self):
        subtotal=sum([i.price for i in self.product.all()])
        return subtotal
    
    @property
    def cart_total(self):
        print(self.product.all())
        total=sum([i.price for i in self.product.all()])
        return total
    
    @property
    def cart_total_products(self):
        print(self.product.all())
        total_products=len(self.product.all())
        return total_products
