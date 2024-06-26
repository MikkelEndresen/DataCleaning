from django.shortcuts import render

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import UploadFileForm
from .utils import datafile_to_df
from .infer_data_types import convert_to_dtype, infer_and_convert_data_types

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
        
        df = infer_and_convert_data_types(df)

        # Save df to .csv, keep dtypes
        dtypes = df.dtypes.astype(str).tolist() # TODO: Fix this!
        dtypes = (d+" " for d in dtypes)
        csv = df.to_csv(index=False)

        response = {
            'data': csv,
            'dtypes': dtypes,
            'file_path': file_path,
        }

        #response = Response(csv, content_type='text/csv')
        return Response(response)
        #return Response({'success': True})
    else:
        return Response({'error': 'No file uploaded'}, status=400)
    
@api_view(['POST'])
def select_dtype(request):
    selected_dtypes = request.data.get('dtypes')
    file_path = request.data.get('file_path')
    try:
        df = datafile_to_df(file_path)
    except ValueError as e:
        return Response({'error': f'{e}'})

    print(selected_dtypes)
    df = convert_to_dtype(selected_dtypes, df)

    # Save df to .csv, keep dtypes
    dtypes = df.dtypes.astype(str).tolist()
    print(dtypes)
    dtypes = (d+" " for d in dtypes)
    csv = df.to_csv(index=False)
    response = {
            'data': csv,
            'dtypes': dtypes,
            'file_path': file_path,
    }
    return Response(response)