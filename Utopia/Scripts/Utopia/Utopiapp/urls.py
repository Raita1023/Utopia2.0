from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.HomePage, name='HomePage'),
    path('Service', views.Service, name='Service'),
    path('News', views.News, name='News'),
    path('Tickets', views.Tickets, name='Tickets'),
    path('About', views.About, name='About'),
    path('Contact', views.Contact, name='Contact'),
    path('Entry', views.Entry, name='Entry'),
]
