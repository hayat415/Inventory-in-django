from django.contrib import admin
from .models import*
admin.site.site_header="hayat"


# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Sale)
admin.site.register(Cart)

