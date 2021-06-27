from django.shortcuts import render

from rest_framework.views import APIView

from .models import Course
# Create your views here.

class ListCourses(APIView):
    def get(self, request, format=None):
        courses = [course.name for course in Course.objects.all()]
        return Response(courses)

class AddCourse(APIView):
    def post(self, request, format=None):
        return Response()

class DeleteCourse(APIView):
    def delete(self, request, format=None):
        return Response()

class UpdateCourse(APIView):
    def update(self, request, pk, format=None):
        return Response()

