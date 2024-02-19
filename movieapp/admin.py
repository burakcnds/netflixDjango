from django.contrib import admin
from .models import *

# Register your models here

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Movie,CategoryAdmin)