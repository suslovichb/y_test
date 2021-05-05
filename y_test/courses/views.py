from .models import Course
from django.http import JsonResponse
from django.views import View
from django.forms.models import model_to_dict
import json


class CoursesGeneralView(View):
    def get(self, request):
        queryset = Course.objects.all()
        try:
            filter_params = json.loads(request.body)["filters"]
            queryset = queryset.filter(**filter_params)
        finally:
            return JsonResponse({'endpoint': 'courses_get', 'data': list(queryset.values()), "status": "success"})

    def post(self, request):
        course_data = json.loads(request.body)
        try:
            new_course = Course(**course_data)
            new_course.save()
            return JsonResponse({'endpoint': 'courses_post', 'status': 'success'})
        except:
            return JsonResponse({'endpoint': 'courses_post', 'status': 'failure'})


class CoursesInstanceView(View):
    def get(self, request, course_id):
        try:
            course_data = Course.objects.get(pk=course_id)
            return JsonResponse({'endpoint': 'course_get', 'data': model_to_dict(course_data), 'status': 'success'})
        except:
            return JsonResponse({'endpoint': 'course_get', 'status': 'failure', })

    def delete(self, request, course_id):
        try:
            course_to_delete = Course.objects.get(pk=course_id)
            course_to_delete.delete()
            return JsonResponse({'endpoint': 'course_delete', 'status': 'success'})
        except:
            return JsonResponse({'endpoint': 'course_delete', 'status': 'failure'})

    def put(self, request, course_id):
        try:
            course_to_update = Course.objects.get(pk=course_id)
            update_data = json.loads(request.body)
            for attr, value in update_data.items():
                setattr(course_to_update, attr, value)
            course_to_update.save()
            return JsonResponse({'endpoint': 'course_put', 'status': 'success'})
        except:
            return JsonResponse({'endpoint': 'course_put', 'status': 'failure'})
