from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('articles/', views.index, name='index'),
    path('<int:pk>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
]
