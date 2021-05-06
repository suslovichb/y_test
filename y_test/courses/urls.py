from django.urls import path
from . import views as courses_views

urlpatterns = [
    path('', courses_views.CoursesGeneralView.as_view(), name='courses'),
    path('<int:course_id>', courses_views.CoursesInstanceView.as_view(), name='course_by_id'),
]
