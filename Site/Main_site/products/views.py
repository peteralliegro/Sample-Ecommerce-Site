from django.shortcuts import render, get_object_or_404
from shoppingcart.models import Cart
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.http import Http404
from urllib import request


from .models import Product

def ProductListPage(request):
    queryset = Product.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, "product_list.html", context)

class ProductDetailPage(DetailView):
    template_name = "product_detail.html"
    queryset = Product.objects.all()


class ProductDetailSlugView(DetailView):
    template_name = "product_detail.html"
    queryset = Product.objects.all()

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404("Not Found")
        except Product.MultipleObjectsReturned:
            queryset = Product.objects.filter(slug=slug, active=True)
            instance = queryset.first()
        except:
            raise Http404("???")
        return instance

    def get_context(self, *args, **kwargs):
        context = super().get_context(self, *args,**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context
    
    


# Create your views here.
