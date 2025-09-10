from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Question, Answer

class QuestionAPITests(APITestCase):
    def setUp(self):
        self.question = Question.objects.create(text="Test question")

    def test_create_question(self):
        url = reverse('question-list')
        data = {'text': 'Second Test question'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 2)
        new_question = Question.objects.get(text='Second Test question')
        self.assertEqual(new_question.text, 'Second Test question')

    def test_create_answer(self):
        url = reverse('answer-create', args=[self.question.id])
        data = {'text': 'Test answer', 'user_id': 'user_nickname'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Answer.objects.count(), 1)

    def test_create_answer_invalid_user_id(self):
        url = reverse('answer-create', args=[self.question.id])
        data = {'text': 'Test answer', 'user_id': ''}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('user_id', response.data)