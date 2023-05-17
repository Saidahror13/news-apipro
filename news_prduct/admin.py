from django.contrib import admin

# Register your models here.
from news_prduct.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
