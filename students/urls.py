from django.conf.urls import url
from django.urls import path

from .views import (
    StudentListAPIView,
    StudentsAPIView
)

urlpatterns = [
    path('', StudentListAPIView.as_view()),
    path('<int:student_id>/', StudentsAPIView.as_view())
]

