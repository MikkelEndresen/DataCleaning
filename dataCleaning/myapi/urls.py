from django.urls import path
from . import views

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
    path('upload-document/', views.upload_document, name='upload_document'),
    path('select-dtype/', views.select_dtype, name='select-dtype'),
]