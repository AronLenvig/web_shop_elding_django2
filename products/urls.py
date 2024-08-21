from django.urls import path, re_path
from . import views

app_name = "products"

urlpatterns = [
    # path('products/', views.IndexView.as_view(), name="index"),
    re_path(r'^category/(?P<category_path>.+)/$', views.CategoryView.as_view(), name="category"),
    path('products/<str:SKU>/', views.ProductDetailView.as_view(), name="details"),
]
