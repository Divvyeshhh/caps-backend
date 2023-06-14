from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Caps)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Business)
admin.site.register(Package)