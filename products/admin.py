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

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(ProductBulletPoint)
admin.site.register(ProductSpecification)