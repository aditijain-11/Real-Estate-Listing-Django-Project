from django.contrib import admin
from .models import Listing
# Register your models here.

# below line brings listing to django admin
admin.site.register(Listing)
