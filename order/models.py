from django.db import models
from cart.models import Cart
from address.models import Address

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)

class Order(models.Model):
    cart                = models.ForeignKey(Cart, on_delete=models.CASCADE)
    delivery_address    = models.ForeignKey(Address,on_delete=models.CASCADE, related_name="delivery")
    active              = models.BooleanField(default=True)
    status              = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    timestamp           = models.DateTimeField(auto_now=True)
    updated             = models.DateTimeField(auto_now=True)
    shipping_total      = models.DecimalField(default=25, max_digits=100, decimal_places=2)
    total               = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    class Meta:
        db_table = "order"

    def __str__(self):
        return str(self.id)