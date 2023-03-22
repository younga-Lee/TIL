from django.urls import path
from . import views

app_name ='certifications'
urlpatterns = [
    path('certification1/', views.certification1, name='certification1'),
    path('certification2/', views.certification2, name='certification2'),
    path('certification3/', views.certification3, name='certification3'),
        
]
