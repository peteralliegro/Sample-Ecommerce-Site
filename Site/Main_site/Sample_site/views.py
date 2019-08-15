from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def home_page(request):
    return render(request, "home_page.html",{})



def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    return response