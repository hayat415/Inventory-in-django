from django.contrib import messages
from django.http import JsonResponse
import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import*
from .forms import AddOrderForm, AddSale, AddProductForm, AddCartForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required(login_url='login')
def index (request):
    product=Product.objects.all()
    order=Order.objects.all()
    sale=Sale.objects.all()
    context={
        'product':product,
        'orders':order,
        'sales':sale
        }
    return render (request, "dashboard/index.html", context)
@login_required(login_url='login')
def CartCreate(request):
    if request.method=='POST':
        form=AddCartForm(request.POST)
        if form.is_valid():
            product_id=form.cleaned_data['product_id']
            quantity=form.cleaned_data['quantity']
            product=get_object_or_404(Product, pk=product_id)
            
            cart_id=request.session.get('cart_id')
            if cart_id:
                cart_ob=Cart.objects.get(id=cart_id)
                this_product_in_cart=cart_ob.sale_set.filter(product=product)
                if this_product_in_cart.exists():
                    cartsale=this_product_in_cart.last()
                    cartsale.quantity += quantity
                    cartsale.sub_total += product.price
                    cartsale.save()
                    cart_ob.total+=cartsale.sub_total
                    cart_ob.save()
                else:
                    cartsale=Sale.objects.create(cart=cart_ob, product=product, quantity=quantity)
                    cartsale.save()
                    cart_ob.total+=cartsale.sub_total
                    cart_ob.save()
            else:
                cart_ob=Cart.objects.create(total=0)
                request.session['cart_id']=cart_ob.id
                salesale=Sale.objects.create(cart=cart_ob, product=product, quantity=quantity)
                salesale.save()
                cart_ob.total+=salesale.sub_total
                cart_ob.save()
                return redirect('cart')


    else:
        form=AddCartForm(request.POST)
    cart_id=request.session.get('cart_id')
    if cart_id:
        carts=Cart.objects.get(id=cart_id)
    else:
        carts=None

    context={
        "form":form,
        
        "carts":carts
        }
    return render(request, "dashboard/cart.html", context)


@login_required(login_url='login')
def SaleProduct (request):
    grand_total = Sale.objects.aggregate(total=Sum('sub_total'))['total']
    total=Sale.objects.values('created_at').annotate(grand_total=Sum('sub_total'))
    sale_product=Sale.objects.all().order_by('-created_at')
    current_date=timezone.now().date()
    sale_count=Sale.objects.filter(created_at=current_date).count()
   
    context={
        "sales":sale_product,
        "total":grand_total,
       
        "gtotals":total,
        "salecount":sale_count,
        }
    return render(request, "dashboard/sale.html", context)
@login_required(login_url='login')
def DeleteSale(request, pk):
    saleitem=Sale.objects.get(id=pk)
    saleitem.delete()
    return redirect('sale')
@login_required(login_url='login')
def EditSale(request, pk):
    edititem=Sale.objects.get(id=pk)
    if request.method=='POST':
        form=AddSale(request.POST, instance=edititem)
        edititem.save()
        return redirect("sale")
    else:
       form=AddSale()
       context={
           'form':form
       }
    return render(request, "dashboard/update.html", context)
@login_required(login_url='login')
def SaleDelete(request, pk):
    saledel=Sale.objects.get(id=pk)
    saledel.delete()
    return redirect("sale")

    
        
@login_required(login_url='login')
def product(request):
    product_list=Product.objects.all().order_by("created_at")
    
    product_count=product_list.count()
    if request.method=="POST":
        add_product=AddProductForm(request.POST)
        if add_product.is_valid():
            add_product.save()
            return redirect('product') 
    else:
        add_product=AddProductForm()

    context={
        'product':product_list,
        'form':add_product,
        'count':product_count
        }
    return render(request, "dashboard/product.html", context)
@login_required(login_url='login')
def OrderView(request):
    order=Order.objects.all()
    current_data=timezone.now().date()
    order_count=order.filter(created_at__date=current_data).count()
    if request.method=='POST':
        add_order=AddOrderForm(request.POST)
        if add_order.is_valid():
            add_order.save()
            return redirect("order")
    else:
        add_order=AddOrderForm()

    context={
        'orders':order,
        'form': add_order,
        'order_count':order_count
        }
    return render(request, "dashboard/order.html", context)
@login_required(login_url='login')
def DeleteProduct(request, pk):
    item=Product.objects.get(id=pk)
    item.delete()
    return redirect("product")
@login_required(login_url='login')    
def EditProduct(request, pk):
    item=Product.objects.get(id=pk)
    if request.method=='POST':
        form=AddProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("product")
    else:
        form=AddProductForm(instance=item)
    context={
        'form':form
    }
    return render(request, "dashboard/update.html", context)     
@login_required(login_url='login')
def Export_data(request):
    objs=Sale.objects.all()
    data=[]
    for obj in objs:
        data.append({
            "product":obj.product,
            "quantity":obj.quantity,
            "price":obj.product.price,
            "sub_total":obj.sub_total,
            "created_at": obj.created_at
        })
    pd.DataFrame(data).to_excel('output.xlsx')
    
    return redirect("sale" )
@login_required(login_url='login')
def CheckOut(request):
    del request.session['cart_id']
    return redirect("sale")
 
  
@login_required(login_url='login')
def PrintReceipt(request):
    sales=Cart.objects.last()
    
    return render(request, "dashboard/receipt.html",{'receipt':sales})
    
