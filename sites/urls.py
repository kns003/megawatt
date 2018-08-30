from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sites/<int:site_id>/', views.detail, name='detail'),
    path('sites/summary/', views.summary, name='summary'),
    path('sites/summary-average/', views.summary_avarage, name='summary_average')
]