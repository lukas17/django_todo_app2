from django.urls import path
from todo.views import AboutView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall'),
    path('about/', AboutView.as_view()),
    path('app2/', views.index, name='app2'),
    path('app3/', views.app3, name='app3'),
    path('app3/add3', views.addTodo3, name='add3'),
    path('app3/complete3/<todo_id>', views.completeTodo3, name='complete3'),
    path('app3/deletecomplete3', views.deleteCompleted3, name='deletecomplete3'),
    path('app3/deleteall3', views.deleteAll3, name='deleteall3'),
]
