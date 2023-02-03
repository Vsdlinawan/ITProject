from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('services/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('handle_login/', views.handle_login, name='handle_login'),
    path('handle_signin/', views.handle_signin, name='handle_login'),
    path('handle_logout/', views.handle_logout, name='handle_logout'),
    path('handle_booking/', views.handle_booking, name='handle_booking'),
    path('handle_voting/', views.handle_voting, name='handle_voting'),
    path('handle_document/', views.handle_document, name='handle_voting'),
    path('administration/', views.administration, name='administration'),
    path('handle_deletion/', views.handle_deletion, name='handle_deletion')
]