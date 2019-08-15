from django.shortcuts import render, redirect
from .models import Cart
from django.shortcuts import get_object_or_404
from products.models import Product as Product


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'cart_page.html', {"cart": cart_obj})


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        product_obj = Product.objects.get(id=product_id)
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
            cart_obj.products.quantity=-1
        print(product_obj)
    return redirect("cart:home")
   
    

# Create your views here.
