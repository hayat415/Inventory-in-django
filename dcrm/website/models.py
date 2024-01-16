from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.PositiveIntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.id},{self.name}"
class Cart(models.Model):
    total=models.BigIntegerField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

class Sale(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(null=True)
    sub_total=models.PositiveBigIntegerField(editable=False, null=True)
    total=models.PositiveBigIntegerField(editable=False, default=0)
    created_at=models.DateField(auto_now_add=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        self.sub_total=self.quantity * self.product.price
        self.total=self.total + self.sub_total
        super(Sale, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.product}"
class Order (models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(null=True)
    customer=models.CharField(max_length=50, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"{self.product.name}"



    
