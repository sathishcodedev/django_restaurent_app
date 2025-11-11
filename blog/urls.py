from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.index, name="index_page"),
    path('text/', views.textview, name="text_page"),
    path('detail/<int:id>/',views.detailview, name='detail_page'),
]