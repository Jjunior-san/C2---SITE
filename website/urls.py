from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('software/', views.software, name='software'),
    path('marketing/', views.marketing, name='marketing'),
    path('infraestrutura/', views.infraestrutura, name='infraestrutura'),
    path('suporte/', views.suporte, name='suporte'),
    path('contato/', views.contato, name='contato'),
    path('updates/', views.updates, name='updates'),
    path('p/<slug:slug>/', views.dynamic_page, name='dynamic_page'),
]
