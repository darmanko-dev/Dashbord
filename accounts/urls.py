from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index , name='index'),
    
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
     
    
    path('products/', views.product, name='products'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),
    path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),   
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),   
]
