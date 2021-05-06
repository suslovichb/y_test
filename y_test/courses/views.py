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
            return JsonResponse({'message': 'courses loaded', 'data': list(queryset.values()), "status": "success"})

    def post(self, request):
        course_data = json.loads(request.body)
        try:
            new_course = Course(**course_data)
            new_course.save()
            return JsonResponse({'message': 'course added', 'status': 'success'})
        except:
            return JsonResponse({'message': 'course addition failed', 'status': 'failure'})


class CoursesInstanceView(View):
    def get(self, request, course_id):
        try:
            course_data = Course.objects.get(pk=course_id)
            return JsonResponse({'message': 'course info loaded', 'data': model_to_dict(course_data), 'status': 'success'})
        except:
            return JsonResponse({'message': 'course loading failed', 'status': 'failure', })

    def delete(self, request, course_id):
        try:
            course_to_delete = Course.objects.get(pk=course_id)
            course_to_delete.delete()
            return JsonResponse({'message': 'course deleted', 'status': 'success'})
        except:
            return JsonResponse({'message': 'course deletion failed', 'status': 'failure'})

    def put(self, request, course_id):
        try:
            course_to_update = Course.objects.get(pk=course_id)
            update_data = json.loads(request.body)
            for attr, value in update_data.items():
                setattr(course_to_update, attr, value)
            course_to_update.save()
            return JsonResponse({'message': 'course info updated', 'status': 'success'})
        except:
            return JsonResponse({'message': 'course updating failed', 'status': 'failure'})
