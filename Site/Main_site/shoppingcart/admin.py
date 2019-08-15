from django.contrib import admin

# Register your models here.

from .models import Cart


admin.site_header = 'Cartoon Glasswork Admin'

admin.site.register(Cart)