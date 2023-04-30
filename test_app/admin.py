from django.contrib import admin
from test_app.models import Test

#admin.site.register(Account)
admin.site.register(Test) # admin 사이트 화면에 추가

# 여기에 코드를 작성해 줘야 admin화면에서 test table을 정상적으로 조작할 수 있음.
