from django.urls import path
from . import views as courses_views

urlpatterns = [
    path('', courses_views.CoursesGeneralView.as_view()),
    path('<int:course_id>', courses_views.CoursesInstanceView.as_view()),
]
