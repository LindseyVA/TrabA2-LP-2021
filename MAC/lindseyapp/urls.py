from django.urls import path
from django.urls.conf import include
from lindseyapp import views

urlpatterns = [
    path('', views.index, name='teste'),
    path('analise/<str:param>', views.view_dinamica_str, name='dinamica_str'),
    
]