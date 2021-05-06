from django.test import TestCase, Client
from django.urls import reverse
from .models import Course
from django.forms.models import model_to_dict
from datetime import datetime
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.mock_course_id = 1
        self.mock_course = Course.objects.create(
            id=self.mock_course_id,
            name='course1',
            start_date='2021-05-01',
            end_date='2021-05-08',
            lectures_number=5
        )
        self.mock_course_url = reverse('course_by_id', args=[self.mock_course_id])
        self.courses_url = reverse('courses')

    def test_course_list_GET(self):
        response = self.client.get(self.courses_url)
        self.assertEquals(response.status_code, 200)

    def test_course_detail_GET(self):
        response = self.client.get(self.mock_course_url)
        self.assertEquals(response.status_code, 200)

    def test_course_detail_PUT(self):
        put_data = {
            'name': '1st course',
            'start_date': '2021-11-01',
            'end_date': '2021-12-08',
            'lectures_number': 6
        }

        # old_values = model_to_dict(sCourse.objects.get(id=self.mock_course_id))

        response = self.client.put(
            self.mock_course_url,
            json.dumps(put_data),
            content_type="application/json"
        )

        new_values = model_to_dict(Course.objects.get(id=self.mock_course_id))

        self.assertEqual(new_values['name'], put_data['name'])
        self.assertEqual(new_values['start_date'], datetime.strptime(put_data['start_date'], '%Y-%m-%d').date())
        self.assertEqual(new_values['end_date'], datetime.strptime(put_data['end_date'], '%Y-%m-%d').date())
        self.assertEqual(new_values['lectures_number'], put_data['lectures_number'])
        self.assertEquals(response.status_code, 200)


