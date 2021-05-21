from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # 첫번째 URL패턴
]