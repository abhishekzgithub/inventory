from django.db import models
from product.models import Product
from django.conf import settings
from django.db.models.signals import pre_save, post_save, m2m_changed, pre_delete, post_delete
from decimal import Decimal

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
    #Cart.objects.annotate(total=Count('product'))
    @property
    def get_total(self):
        from django.db.models import Count
        #Cart.objects.prefetch_related("product")
        return Cart.objects.annotate(total=Count('product'))

# def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
#     print(sender,instance,action)
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
#     print(sender)
#     # if instance.subtotal > 0:
#     #     instance.total = 1#Decimal(instance.subtotal) * Decimal(1.08) # 8% tax
#     # else:
#     #     instance.total = 0.00

# pre_save.connect(pre_save_cart_receiver, sender=Cart)