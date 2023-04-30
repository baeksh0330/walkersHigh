from django.contrib import admin
from django.urls import path, re_path # django 4부터 url 가져오기가 없어졌다.
from django.urls import include
app_name = 'test_app'
urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework_category')),
]

# does not appear to have any patterns in it.
# If you see valid patterns in the file then the issue is probably caused by a circular import.
# 이거 ... urlpatterns의 p를 대문자로 써서 발생한 에러다 ...