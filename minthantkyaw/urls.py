from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("education", views.education, name="education"),
    path("skills", views.skills, name="skills"),
    path("projects", views.projects, name="projects"),
    path("contact", views.contact, name="contact"),
]