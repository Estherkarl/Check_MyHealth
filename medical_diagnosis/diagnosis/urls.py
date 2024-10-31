from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('diagnose/', views.diagnose_view, name='diagnose'),  # Page de diagnostic
    path('symptoms/', views.symptoms_info, name='symptoms_info'),  # Informations sur les symptômes
]
