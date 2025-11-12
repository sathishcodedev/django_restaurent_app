from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.index, name="index_page"),
    path('text/', views.textview, name="text_page"),
    path('detail/<int:id>/',views.detailview, name='detail_page'),
    path('cart/',views.cartview,name="cart_page"),
    path('cartdetails/<str:slug>/',views.cartproductdetail,name="cartdetail_page"),
    path('cart/update/<int:id>/', views.update_cart, name="update_cart")
]