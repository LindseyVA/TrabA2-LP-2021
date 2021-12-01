from django.urls import path
from Me_Ajuda_Chefe import views

urlpatterns = [
    path('', views.index, name='index')
]
