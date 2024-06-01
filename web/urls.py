from django.urls import path
from . import views

app_name='app'
urlpatterns = [
    path('home/', views.view_home, name='view_home'),
    path('', views.view_login, name='view_login'),
    path('login/', views.view_login, name='view_login'),
    path('logout/', views.view_logout, name='view_logout'),
    path('register/', views.view_register, name='view_register'),
    path('sales/', views.view_sale, name='view_sale'),
    path('inventory/', views.view_inventory, name='view_inventory'),
    path('inventory/create', views.view_inventory_form, name='view_inventory_form'),
    path('inventory/delete/<int:id>', views.view_inventory_delete, name='view_inventory_delete'),
    path('customer/', views.view_customer, name='view_customer'),
    path('customer/create', views.view_customer_form, name='view_customer_form'),

]
