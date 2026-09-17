from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('card/<slug:slug>/<str:plan>/', views.card_detail, name='card_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('success/', views.success_page, name='success'),
    path('activate/', views.activate_membership_api, name='activate'),
]