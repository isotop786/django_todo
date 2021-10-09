
from django.urls import path,include
from .views import list_todo, add_todo, update_todo,delete_todo

urlpatterns = [
  
    path('',list_todo, name="list_todo" ),
    path('add/', add_todo, name="add_todo"),
    path('<int:pk>/update', update_todo, name="update_todo"),
    path('<int:pk>/delete', delete_todo, name="delete_todo"),
    
]
