from django.urls import path, re_path
from . import views

app_name = "products"

urlpatterns = [
    path('products/', views.IndexView.as_view(), name="index"),
    re_path(r'^(?P<category_path>(?:[\w-]+/)*[\w-]+)/$', views.CategoryView.as_view(), name="category"),
    re_path(r'^(?P<category_path>(?:[\w-]+/)*[\w-]+)/(?P<SKU>[\w-]+)/$', views.ProductDetailView.as_view(), name="details"),
]
