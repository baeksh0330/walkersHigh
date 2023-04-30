# 모델과 1:1 매칭되는 serializer를 작성해주어야 함
# model 객체와 querysets같은 데이터를 JSON, XML과 같은 네이티브 데이터로 바꿔주는 역할을 한다.
from rest_framework import serializers # 직렬화 장치
from test_app.models import Test

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('test','id')
        # fields : Person안의 field중 표시하고 싶은 것들을 순서대로 써주면 됨
        # id는 자동 생성됨.