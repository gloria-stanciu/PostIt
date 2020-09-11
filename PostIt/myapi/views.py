# from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from .serializers import PostItSeralizer
from .models import PostIt

# Create your views here.


class PostItView(viewsets.ModelViewSet):
    queryset = PostIt.objects.all().order_by('created')
    serializer_class = PostItSeralizer


# @api_view(['GET', 'POST'])
# def postit(request):
#     if request.method == 'GET':
#         postit = PostIt.objects.all()
#         postit_serializer = PostItSeralizer(postit, many=True)
#         # safe is False for object serialization
#         return JsonResponse(postit_serializer.data, safe=False)
#     elif request.method == 'POST':
#         postit_data = JSONParser().parse(request)
#         postit_serializer = PostItSeralizer(data=postit_data)
#         if postit_serializer.is_valid():
#             postit_serializer.save()
#             return JsonResponse(postit_serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(postit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def postit_details(request, pk):
    try:
        postit = PostIt.objects.get(pk=pk)
    except PostIt.DoesNotExist:
        return JsonResponse(
            {'Message': 'The post-it does not exist'},
            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        postit_serializer = PostItSeralizer(postit)
        return JsonResponse(postit_serializer.data)
    if request.method == 'PUT':
        postit_data = JSONParser().parse(request)
        postit_serializer = PostItSeralizer(postit, data=postit_data)
        if postit_serializer.is_valid():
            postit_serializer.save()
            return JsonResponse(postit_serializer.data)
        return JsonResponse(postit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        postit.delete()
        return JsonResponse(
            {'Message': 'Postit was deleted successfully!'},
            status=status.HTTP_204_NO_CONTENT)
