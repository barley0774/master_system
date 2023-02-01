from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Scenario)
admin.site.register(Term)
admin.site.register(Category)