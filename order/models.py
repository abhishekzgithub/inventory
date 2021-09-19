from django.db import models
from django.conf import settings
from cart.models import Cart
from address.models import Address

User = settings.AUTH_USER_MODEL
ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)

class Order(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    cart                = models.ForeignKey(Cart, on_delete=models.CASCADE)
    delivery_address    = models.CharField(max_length=120, null=True, blank=True)
    active              = models.BooleanField(default=True)
    status              = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    coupon              = models.CharField(max_length=120, null=True, blank=True)
    discount            = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    shipping_cost       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total               = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    created_timestamp = models.DateTimeField(auto_now=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = "order"
        ordering = ['-updated_timestamp']