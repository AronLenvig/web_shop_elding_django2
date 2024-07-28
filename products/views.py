from django.http import Http404
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Product
from django.views import generic
# Create your views here.


class IndexView(generic.ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_queryset()

        # Create a list of products with their first image
        products_with_images = []
        for product in products:
            first_image_url = product.images.first().image.url if product.images.exists() else 'default_image_url'
            product_data = {
                'product': product,
                'first_image_url': first_image_url
            }
            products_with_images.append(product_data)

        context['products_with_images'] = products_with_images
        return context


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/details.html'
    context_object_name = 'product'
    slug_field = 'SKU'
    slug_url_kwarg = 'SKU'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['images'] = product.images.all()
        context['bullet_points'] = product.bullet_points.all()
        context['specifications'] = product.specifications.all()
        return context