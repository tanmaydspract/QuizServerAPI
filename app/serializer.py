from re import A
from rest_framework import serializers

from .models import quizes, questions, answers

class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = quizes
        fields=['title',]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = answers
        fields=['id','answer_text','is_right',]

class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = questions
        fields=['title','answer',]

class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = questions
        fields=['quiz','title','answer',]
