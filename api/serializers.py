from rest_framework import serializers
from .models import Question, Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question_id', 'user_id', 'text', 'created_at']
        read_only_fields = ['id', 'created_at']

class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'created_at']
        read_only_fields = ['id', 'created_at']

class QuestionWithAnswersSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'created_at', 'answers']
        read_only_fields = ['id', 'created_at', 'answers']

class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Question text cannot be empty")
        return value

class AnswerCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=True) 

    class Meta:
        model = Answer
        fields = ['text', 'user_id']
    
    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Answer text cannot be empty")
        return value
    
    def validate_user_id(self, value):
        if not value:
            raise serializers.ValidationError("user_id cannot be empty")
        if not value.strip():
            raise serializers.ValidationError("No user specified")
        return value
