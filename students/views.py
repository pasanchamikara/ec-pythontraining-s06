from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json

from rest_framework.views import APIView
from .models import Student
# Create your views here.

class StudentListAPIView(APIView):
    def get(self, request, format=None):
        students = Student.objects.values()
        # students_json = serializers.serialize('json', students)
        print(list(students))
        students_list = list(students)
        return JsonResponse(students_list, safe=False)
    def post(self, request, format=None):
        st_fname = request.data["fname"]
        st_lname = request.data["lname"]
        st_dob = request.data["dob"]
        st_city = request.data["city"]

        student = Student.objects.create(fname=st_fname, lname=st_lname, dob=st_dob, city=st_city)
        student.save()

        return JsonResponse({"studentId": student.id})
class StudentsAPIView(APIView):
    def get(self, request, student_id):
        student = Student.objects.get(id=student_id)
        serialized_student = serializers.serialize('json', [student,])
        return JsonResponse(serialized_student, safe=False)

    def post(self, request, format=None):
        st_fname = request.data["fname"]
        st_lname = request.data["lname"]
        st_dob = request.data["dob"]
        st_city = request.data["city"]

        student = Student.objects.Create(fname=st_fname, lname=st_lname, dob=st_dob, city=st_city)
        student.save()

        return student.id
    def put(self, request, format=None):
        # student = Student.objects.get(id=)
        return
    def delete(self, request, format=None):
        return
