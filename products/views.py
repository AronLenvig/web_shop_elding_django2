from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product, Category

class IndexView(generic.ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_queryset()

        # Create a list of products with their first image and category path
        products_with_images = []
        for product in products:
            first_image_url = product.images.first().image.url if product.images.exists() else 'default_image_url'
            product.price = round(product.price)

            # Build the category path
            category = product.category
            if category:
                category_path = []
                while category:
                    category_path.append(category.slug)
                    category = category.parent
                category_path = '/'.join(reversed(category_path))
            else:
                category_path = None

            product_data = {
                'product': product,
                'first_image_url': first_image_url,
                'category_path': category_path
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

    def get_object(self):
        SKU = self.kwargs['SKU']
        return get_object_or_404(Product, SKU=SKU)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
        category_path = self.kwargs.get('category_slug').split('/')
        category_slug = category_path[-1]
        category = get_object_or_404(Category, slug=category_slug)
        categories = [category] + category.get_descendants()
        return Product.objects.filter(category__in=categories)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_queryset()

        # Create a list of products with their first image and category path
        products_with_images = []
        for product in products:
            first_image_url = product.images.first().image.url if product.images.exists() else 'default_image_url'
            product.price = round(product.price)

            # Build the category path
            category = product.category
            if category:
                category_path = []
                while category:
                    category_path.append(category.slug)
                    category = category.parent
                category_path = '/'.join(reversed(category_path))
            else:
                category_path = ''

            product_data = {
                'product': product,
                'first_image_url': first_image_url,
                'category_path': category_path
            }
            products_with_images.append(product_data)

        context['products_with_images'] = products_with_images
        context['category'] = get_object_or_404(Category, slug=self.kwargs.get('category_slug').split('/')[-1])
        return context