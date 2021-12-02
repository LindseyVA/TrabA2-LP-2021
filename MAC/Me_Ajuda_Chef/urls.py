from django.urls import path
from Me_Ajuda_Chef import views

urlpatterns = [
    path('', views.index, name='index')
]
