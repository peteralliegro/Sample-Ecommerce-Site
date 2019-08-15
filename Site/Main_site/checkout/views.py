from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def checkout_page(request):
    return render(request, "checkout_page.html",{})
