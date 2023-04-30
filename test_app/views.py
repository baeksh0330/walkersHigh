from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from test_app.models import Test
from test_app.serializers import TestSerializer

class TestViewSet(viewsets.ModelViewSet):
    querySet = Test.objects.all() # Test클래스 안의 모든 것을 queryset으로 저장
    serializer_class = TestSerializer