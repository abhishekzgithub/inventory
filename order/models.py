from django.db import models
from django.conf import settings
from cart.models import Cart
from address.models import Address
from product.models import Product
from services.models import Services

User = settings.AUTH_USER_MODEL
ORDER_STATUS_CHOICES = (
    ('created', 'Order Made'),
    ('inprocess', 'In-process'),
    ('pending', 'Pending'),
    ('complete', 'Complete'),
    ('invalid', 'Invalid'),
    ('returned', 'Returned'),
)

class OrderItem(models.Model) :
    user            = models.ForeignKey(User,on_delete=models.CASCADE)
    product         = models.ForeignKey(Product, on_delete=models.CASCADE)
    services        = models.ForeignKey(Services, on_delete=models.CASCADE)
    quantity        = models.PositiveIntegerField(blank=True, null=True, default=1)
    ordered         = models.BooleanField(default=False)
    def __str__(self):
        return str(str(self.product)+"-+-"+str(self.services))
    
    class Meta:
        db_table = "order_item"


class Order(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    items               = models.ManyToManyField(OrderItem) # this will be many to many
    delivery_address    = models.CharField(max_length=120, null=True, blank=True)
    active              = models.BooleanField(default=True)
    status              = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    delivery_charge     = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    delivery_date       = models.DateTimeField(auto_now=True)
    notes               = models.TextField(blank = True)
    discount            = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total               = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    created_timestamp   = models.DateTimeField(auto_now=True)
    updated_timestamp   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = "order"
        ordering = ['-updated_timestamp']