from django.urls import path
from django.urls.conf import include
from lindseyapp import views as lindseyapp_views
urlpatterns = [
    path('', lindseyapp_views.index, name='teste'),
    path('special/<str:param>', lindseyapp_views.view_dinamica_str, name='dinamica_str'),
    path('special/<int:param>', lindseyapp_views.view_dinamica_int, name='dinamica_int'),
    path('analise/', lindseyapp_views.lindsey, name='analise'),   
]