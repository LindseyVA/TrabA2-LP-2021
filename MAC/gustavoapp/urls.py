from django.urls import path
from django.urls.conf import include
from gustavoapp import views as gustavoapp_views 

urlpatterns = [
    path('', gustavoapp_views.index, name='teste'),
    path('special/<int:param>', gustavoapp_views.view_dinamica_int, name='dinamica_int'),
    path('special/<str:param>', gustavoapp_views.view_dinamica_str, name='dinamica_str'),
    path('analise/', gustavoapp_views.gustavo, name='analise'),
]
