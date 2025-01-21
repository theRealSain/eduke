from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('login/', views.login_view, name='login'),  # Login page
    path('register/', views.register_institution, name='institution_register'),  # Registration page
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Admin dashboard
    path('admin/logout/', views.admin_logout, name='admin_logout'),  # Admin logout
]
