from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='tarefas/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('tarefas/nova/', views.criar_tarefa, name='criar_tarefa'),

    path(
        'tarefas/<int:tarefa_id>/concluir/',
        views.concluir_tarefa,
        name='concluir_tarefa'
    ),

    path(
        'tarefas/<int:tarefa_id>/excluir/',
        views.excluir_tarefa,
        name='excluir_tarefa'
    ),
    path('', views.inicio, name='inicio'),
]