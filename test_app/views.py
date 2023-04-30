from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from test_app.models import Test
from test_app.serializers import TestSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all() # Test클래스 안의 모든 것을 queryset으로 저장
    serializer_class = TestSerializer

    #querySet을 set으로 바꿔주니까 오류해결될듯말듯듯