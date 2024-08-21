from django.shortcuts import render
from util import get_category_path
from products.models import Product

def index(request):
    products_with_images = []
    products = Product.objects.all()
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

    return render(request, 'index.html', context={'products_with_images': products_with_images})

def carousel(request):
    return render(request, 'carousel.html')