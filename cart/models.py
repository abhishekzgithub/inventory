from django.db import models
from product.models import Product
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    active  = models.BooleanField(default=True) 
    product = models.ManyToManyField(Product, blank=True)
    created_timestamp = models.DateTimeField(auto_now=True)
    updated_timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)
    
    @property
    def cart_subtotal(self):
        subtotal=sum([i.price for i in self.product.all()])
        return subtotal
    
    @property
    def cart_total(self):
        total=sum([i.price for i in self.product.all()])
        return total
    
    @property
    def cart_total_products(self):
        total_products=len(self.product.all())
        return total_products

    class Meta:
        ordering = ['-updated_timestamp']
        db_table = "cart"