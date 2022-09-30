from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import quizes, questions
from .serializer import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
from app import serializer
# Create your views here.

def show(request):
    return render(request, 'index.html')

class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = quizes.objects.all()

class RandomQuestion(APIView):
    
    def get(self, request, format=None, **kwargs):
        question = questions.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        ser= RandomQuestionSerializer(question, many=True)
        return Response(ser.data)

class QuizQuestion(APIView):
    
    def get(self, request, format=None, **kwargs):
        question = questions.objects.filter(quiz__title=kwargs['topic'])
        ser= QuestionSerializer(question, many=True)
        return Response(ser.data) 