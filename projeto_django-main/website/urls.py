from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    
    path('funcionario/<int:id>/', views.detalhes_funcionario, name='detalhes'),
    
    path('funcionarios/', views.listar_funcionarios, name='listar'),
    
    path('editar_funcionario/<int:id>/', views.editar_funcionario, name='editar_funcionario'),
    
    path('excluir_funcionario/<int:id>/', views.excluir_funcionario, name='excluir_funcionario'),
    
    path('contato/', views.contato, name='contato'),

]