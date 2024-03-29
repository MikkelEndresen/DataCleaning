from django.shortcuts import render

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import UploadFileForm
from .utils import datafile_to_df


@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

@api_view(['POST'])
def upload_document(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        file = form.save()
        file_path = file.file.url
        print(file_path)
        # file to csv
        try:
            df = datafile_to_df(file_path)
        except ValueError as e:
            return Response({'error': f'{e}'})

        print(df)
        return Response({'success': True})
    else:
        return Response({'error': 'No file uploaded'}, status=400)