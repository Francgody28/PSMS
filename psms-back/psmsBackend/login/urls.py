from django.urls import path
from . import views

urlpatterns = [
    # Authentication endpoints
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    # Dashboard endpoints
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Admin user management endpoints
    path('register/', views.register_user, name='register_user'),
    path('users/', views.get_all_users, name='get_all_users'),
    path('users/<int:user_id>/status/', views.update_user_status, name='update_user_status'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    
    # Profile endpoints
    path('profile/', views.get_profile, name='get_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
]
