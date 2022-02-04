from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.renderers import JSONRenderer


def post_summary(request, pk):
    post = Post.objects.get(id=pk)
    post_serializer = PostSerializer(post)
    json_data = JSONRenderer().render(post_serializer.data)

    return HttpResponse(json_data, content_type='application/json')

def post_list(request):
    post = Post.objects.all()
    post_serializer = PostSerializer(post, many=True)
    json_data = JSONRenderer().render(post_serializer.data)

    return HttpResponse(json_data, content_type='application/json')