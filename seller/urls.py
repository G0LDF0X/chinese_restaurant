from django.urls import path
from . import views

app_name='seller'
urlpatterns = [   
    path('', views.seller_index, name='seller_index'),
    path('add_food/', views.add_food, name='seller_add_food'),
    path('detail_food/<int:pk>/', views.detail_food, name='seller_detail_food'),
    path('delete_food/<int:pk>/', views.delete_food, name='seller_delete_food'),
]