from typing import Any, Dict, List, Optional
from django.shortcuts import get_object_or_404
from products.models import Category

def get_category_path(category: Optional[Category]) -> str:
    category_path = []
    if not category:
        return ''
    while category:
        category_path.append(category.slug)
        category = category.parent
    return '/'.join(reversed(category_path))

def get_breadcrumbs_from_category_path(category_path: str) -> List[Dict[str, Any]]:
    breadcrumbs: List[Dict[str: Any]] = []
    if category_path:
        category_slugs = category_path.split('/')
        breadcrumbs = []
        full_path = ""
        
        for slug in category_slugs:
            print("slug", slug)
            full_path += f"{slug}/"
            category = get_object_or_404(Category, slug=slug)
            breadcrumbs.append({
                'name': category.name,
                'url': full_path.rstrip('/'),
            })
            # print("full_path", full_path.strip())
    return breadcrumbs
