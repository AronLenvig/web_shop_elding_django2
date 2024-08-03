from django.urls import path, re_path
from . import views

app_name = "products"

urlpatterns = [
    path('products/', views.IndexView.as_view(), name="index"),
    path("products/<str:SKU>/", views.ProductDetailView.as_view(), name="details"),
    re_path(r'^(?P<category_path>.+)/(?P<SKU>[^/]+)/$', views.ProductDetailView.as_view(), name="details"),
    path('<slug:category_slug>/', views.CategoryView.as_view(), name="category"),
]
