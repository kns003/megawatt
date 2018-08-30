from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:site_id>/', views.detail, name='detail'),
    path('summary/', views.summary, name='summary'),
    path('summary-average/', views.summary_avarage, name='summary_average')
]