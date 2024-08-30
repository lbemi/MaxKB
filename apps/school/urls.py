from django.urls import path

from . import views

app_name = "school"
urlpatterns = [
    path("school", views.School.as_view()),
    path("professional", views.Professional.as_view()),
]
