# from django.shortcuts import render
# from django.views.generic import ListView
from .models import Course
from django.http import JsonResponse
from django.views import View


class CoursesGeneralView(View):
    model = Course

    def get(self, *args, **kwargs):
        return JsonResponse({'endpoint': 'courses_get'})

    def post(self, *args, **kwargs):
        return JsonResponse({'endpoint': 'courses_post'})


class CoursesInstanceView(View):
    def get(self, *args, **kwargs):
        return JsonResponse({'endpoint': 'course_get'})

    def delete(self, *args, **kwargs):
        return JsonResponse({'endpoint': 'course_delete'})
