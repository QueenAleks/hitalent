from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer, AnswerCreateSerializer

class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailView(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer
    
    def perform_create(self, serializer):
        question_id = self.kwargs['question_id']
        question = get_object_or_404(Question, id=question_id)
        serializer.save(question=question)

class AnswerDetailView(generics.RetrieveDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

@api_view(['GET'])
def question_answers(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answers.all()
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)