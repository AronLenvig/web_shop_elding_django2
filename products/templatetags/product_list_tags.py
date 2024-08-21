from django import template

register = template.Library()

@register.inclusion_tag('products/product_list.html')
def product_list_tag(items):
    return {"items": items}
    #item.first_image_url
    #item.category_path
    #item.product.name
    #item.product.price
    #item.product.SKU
    
