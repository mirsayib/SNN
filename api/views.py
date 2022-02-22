from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blog.models import Post
from users.models import Profile
from django.contrib.auth.models import User
from .serializers import (
    PostSerializer,
    BlogSerializer,
    ProfileSerializer,
    UserSerializer,
)
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class PostDetail(APIView):
    """
    retrieve, update or delete a snippet instance

    """
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        stream = io.BytesIO(request.body)
        pythondata = JSONParser().parse(stream)

        serializer = PostSerializer(post, data=pythondata)

        if(serializer.is_valid()):
            serializer.save()
            res = {'msg': 'Post Updated'}
            return Response(res)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def post_list(request, format=None):
    if(request.method=='GET'):
        post = Post.objects.all()
        post_serializer = BlogSerializer(post, many=True)
        return Response(post_serializer.data)


    elif(request.method == 'POST'):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = PostSerializer(data=pythondata)

        if(serializer.is_valid()):
            serializer.save()
            res = {'msg': 'Post Created'}
            return Response(res, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def profile_list(request, format=None):
    if(request.method=='GET'):
        profile = Profile.objects.all()
        profile_serializer = ProfileSerializer(profile, many=True)
        return Response(profile_serializer.data)


    

@api_view(['GET', 'POST'])
def user_list(request, format=None):
    if(request.method=='GET'):
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return Response(user_serializer.data)


    

        
        



