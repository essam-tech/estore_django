# amr/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views   # ✅ لازم هذا السطر

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<slug:category_slug>/", views.product_list, name="product_list"),
    path("product/<slug:product_slug>/", views.product_detail, name="product_detail"),
    path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='cart_add'),


]


