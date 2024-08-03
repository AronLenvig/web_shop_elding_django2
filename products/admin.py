from django.contrib import admin
from .models import Product, Category, ProductImage, ProductBulletPoint, ProductSpecification
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms

# Register your models here.

class ProductAdminForm(forms.ModelForm):
    long_description = forms.CharField(widget=CKEditor5Widget(config_name='default'))

    class Meta:
        model = Product
        fields = '__all__'

class ProductBulletPointInline(admin.TabularInline):
    model = ProductBulletPoint
    extra = 3
    max_num = 3

class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification
    extra = 1

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    inlines = [ProductBulletPointInline, ProductSpecificationInline, ProductImageInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)