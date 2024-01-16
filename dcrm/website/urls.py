from django.urls import path
from .import views
from user import views as user_views

urlpatterns=[
    path("", views.index, name="index"),
    
    path("product/", views.product, name="product"),
    path("order/", views.OrderView, name="order"),
    path("register/", user_views.register, name='register'),
    path("delete/<int:pk>/", views.DeleteProduct, name="delete"),
    path("edit/<int:pk>/", views.EditProduct, name="edit"),
    path("sale/", views.SaleProduct, name="sale"),
    path("export/", views.Export_data, name='export'),
    path("saleedit/<int:pk>/", views.EditSale, name="saleedit"),
    path("saledelete/<int:pk>/", views.SaleDelete, name="saledelete"),
    path("print/", views.PrintReceipt, name="receipt"),
    path("cart/", views.CartCreate, name="cart"),
    path("checkout/", views.CheckOut, name="checkout"),
  
    
]