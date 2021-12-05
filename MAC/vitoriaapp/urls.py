from django.urls import path
from django.urls.conf import include
from vitoriaapp import views as vitoriaapp_views 

urlpatterns = [
    path('', vitoriaapp_views.index, name='teste'),
    path('special/<str:param>', vitoriaapp_views.view_dinamica_str, name='dinamica_str'),
    path('special/<int:param>', vitoriaapp_views.view_dinamica_int, name='dinamica_int'),
    path('analise/', vitoriaapp_views.vitoria, name='analise'),
]