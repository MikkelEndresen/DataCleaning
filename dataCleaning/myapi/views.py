from django.shortcuts import render

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import UploadFileForm


@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

@api_view(['POST'])
def upload_document(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return Response({'success': True})
    else:
        return Response({'error': 'No file uploaded'}, status=400)