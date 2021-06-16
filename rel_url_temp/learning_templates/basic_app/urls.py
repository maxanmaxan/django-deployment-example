from django.urls import path
from basic_app.views import Relative, Other

# Template tagging

app_name = 'basic_app'

urlpatterns = [
    path('relative/', Relative.as_view(), name='relative'),
    path('other/', Other.as_view(), name='other')
]
