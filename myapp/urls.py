from django.urls import path
from myapp import views

urlpatterns = [
    path('studentapi/',views.student_api),
]
