from django.urls import path
from . import views

urlpatterns = [
    path('first_view/', views.first_view, name='first_view'),
    path('pop_view/', views.pop_view, name='pop_view'),
    path('login_consent_view/', views.login_consent_view, name='login_consent'),
    path('callback/', views.callback, name='callback'),
]
