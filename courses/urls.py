from django.conf.urls import url
from django.urls import path

from .views import (
    ListCoursesAPIView,
    CoursesAPIView
)

urlpatterns = [
    path('', ListCoursesAPIView.as_view()),
    path('<int:course_id>/', CoursesAPIView.as_view())
]