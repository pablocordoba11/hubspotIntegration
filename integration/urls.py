from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('token', views.create_token, name='token'),
    path('pullDeals/<str:at>/', views.pull_deals)
]