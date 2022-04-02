from typing import ValuesView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesList.as_view()),
    path('<int:pk>/', views.NotesDetails.as_view()) # api/v1/notes/1
]
