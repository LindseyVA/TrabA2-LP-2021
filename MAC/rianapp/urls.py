from django.urls import path
from django.urls.conf import include
from rianapp import views as rianapp_views

urlpatterns = [
    path('', rianapp_views.index, name='teste'),
    path('special/<int:param>', rianapp_views.view_dinamica_int, name='dinamica_int'),
    path('special/<str:param>', rianapp_views.view_dinamica_str, name='dinamica_str'),
    path('analise/', rianapp_views.rian, name='analise'),
]
