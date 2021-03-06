from django.urls import path
from django.views.static import serve
from Me_Ajuda_Chefe import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('receitas/<str:param>', views.receita, name='receita'),
    path('produtos/', views.produtos, name='produtos'),
    path('minhas-receitas/', views.minhas_receitas, name='minhas-receitas'),
    path('receitas/', views.receitas, name='receitas'),
]
