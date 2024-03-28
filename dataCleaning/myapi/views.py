from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

@api_view(['POST'])
def upload_document(request):
    if request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        # add logic here
        return Response({'success': True})
    else:
        return Response({'error': 'No file uploaded'}, status=400)