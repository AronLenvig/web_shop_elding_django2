from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product, Category
from util import get_category_path, get_breadcrumbs_from_category_path


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/details.html'
    context_object_name = 'product'
    slug_field = 'SKU'
    slug_url_kwarg = 'SKU'

    def get_object(self):
        SKU = self.kwargs['SKU']
        return get_object_or_404(Product, SKU=SKU)

    def get_context_data(self, **kwargs):
        category_path = get_category_path(self.get_object().category)
        breadcrumbs = get_breadcrumbs_from_category_path(category_path)
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = breadcrumbs
        context['product'].price = round(context['product'].price)
        product = self.get_object()
        context['images'] = product.images.all()
        context['bullet_points'] = product.bullet_points.all()
        context['specifications'] = product.specifications.all()
        return context
    
class CategoryView(generic.ListView):
    model = Product
    template_name = 'products/category.html'
    context_object_name = 'products'

    def get_queryset(self):
        # Use category_path instead of category_slug
        category_path = self.kwargs.get('category_path')
          
        if category_path:
            category_slug = category_path.split('/')[-1]
            category = get_object_or_404(Category, slug=category_slug)
            categories = [category] + list(category.get_descendants())
            return Product.objects.filter(category__in=categories)
        else:
            return Product.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_queryset()

        products_with_images = []
        for product in products:
            first_image_url = product.images.first().image.url if product.images.exists() else 'default_image_url'
            product.price = round(product.price)
            category_path = get_category_path(product.category)

            product_data = {
                'product': product,
                'first_image_url': first_image_url,
                'category_path': category_path
            }
            products_with_images.append(product_data)

        breadcrumbs = get_breadcrumbs_from_category_path(self.kwargs.get('category_path'))

        context['products_with_images'] = products_with_images
        context['breadcrumbs'] = breadcrumbs
        if self.kwargs.get('category_path'):
            context['category'] = get_object_or_404(Category, slug=self.kwargs.get('category_path').split('/')[-1])
        return context
