from django.urls import path
from . import views

urlpatterns = [
    path('course_outcomes/', views.outcomes, name='outcomes'),
    path('course_outcomes/insertuser/',views.insertuser, name='insertuser'),
    path('course_outcomes/view_users/',views.view_users,name='view_users'),
]