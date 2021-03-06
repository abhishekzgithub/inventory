from django.db import models
from product.models import Product
from django.conf import settings
from django.db.models.signals import pre_save, post_save, m2m_changed
from decimal import Decimal

User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)
    # subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    # total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "cart"

    def __str__(self):
        return str(self.id)

# def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
#     if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
#         product = instance.product.all()
#         total = 0
#         for x in product:
#             total += x.price
#         if instance.subtotal != total:
#             instance.subtotal = total
#             instance.save()

# m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.product.through)

# def pre_save_cart_receiver(sender, instance, *args, **kwargs):
#     if instance.subtotal > 0:
#         instance.total = Decimal(instance.subtotal) * Decimal(1.08) # 8% tax
#     else:
#         instance.total = 0.00

# pre_save.connect(pre_save_cart_receiver, sender=Cart)