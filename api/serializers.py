from rest_framework import serializers
from .models import Question, Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question_id', 'user_id', 'text', 'created_at']
        read_only_fields = ['id', 'created_at']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'text', 'created_at', 'answers']
        read_only_fields = ['id', 'created_at', 'answers']
    
    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Question text cannot be empty")
        return value

class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text', 'user_id']
    
    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Answer text cannot be empty")
        return value