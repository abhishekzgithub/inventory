from random import choice
from django.db import models
from django.conf import settings
from product.models import Product

User = settings.AUTH_USER_MODEL
ORDER_STATUS_CHOICES = (
    ('created', 'Order Made'),
    ('inprocess', 'In-process'),
    ('pending', 'Pending'),
    ('complete', 'Complete'),
    ('invalid', 'Invalid'),
    ('returned', 'Returned'),
)

ORDER_PAYMENT_METHOD_CHOICES = (
    ('card', 'Card'),
    ('upi', 'UPI'),
    ('cash', 'CASH'),
)

class OrderItem(models.Model) :
    user            = models.ForeignKey(User,on_delete=models.CASCADE)
    product         = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity        = models.PositiveIntegerField(blank=True, null=True, default=1)
    ordered         = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)+"-"+(str(self.product))

    def get_total_item_price(self):
        return self.quantity * self.product.price

    def get_final_price(self):
        return self.get_total_item_price()

    class Meta:
        db_table = "order_item"


class Order(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    items               = models.ManyToManyField(OrderItem) # this will be many to many
    delivery_address    = models.CharField(max_length=120, null=True, blank=True)
    ordered              = models.BooleanField(default=False)
    status              = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    payment_method      = models.CharField(max_length=120,choices=ORDER_PAYMENT_METHOD_CHOICES, default=ORDER_PAYMENT_METHOD_CHOICES[0][0])
    delivery_charge     = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    notes               = models.TextField(blank = True)
    discount            = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total               = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    ordered_date        = models.DateTimeField()
    delivery_date       = models.DateTimeField(null=True, blank=True)
    created_timestamp   = models.DateTimeField(auto_now=True)
    updated_timestamp   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
    
    class Meta:
        db_table = "order"
        ordering = ['-updated_timestamp']