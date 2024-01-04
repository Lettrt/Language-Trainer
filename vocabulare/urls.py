from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('themes/<int:pk>/', views.ThemeBlockDetailView.as_view(), name='theme_detail'),
    path('themes/<int:pk>/add_word', views.AddWordView.as_view(), name='add_word')
]
