from django.urls import path
from django.urls.conf import include
from mathapp import views as mathapp_views 

urlpatterns = [
    path('', mathapp_views.index, name='teste'),
    path('special/<str:param>', mathapp_views.view_dinamica_str, name='dinamica_str'),
    path('special/<int:param>', mathapp_views.view_dinamica_int, name='dinamica_int'),
    path('analise/', mathapp_views.matheus, name='analise'),
]