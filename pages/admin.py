from django.contrib import admin
from pages.models import *




@admin.register(CategoryModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(ProductesModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['title']
    

@admin.register(BookingModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(photoesModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['name']
