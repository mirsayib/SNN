from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blog.models import Post
from .serializers import PostSerializer, BlogSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt


def post_summary(request, pk):
    post = Post.objects.get(id=pk)
    post_serializer = BlogSerializer(post)
    json_data = JSONRenderer().render(post_serializer.data)

    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(post_serializer.data)

def post_list(request):
    post = Post.objects.all()
    post_serializer = BlogSerializer(post, many=True)
    json_data = JSONRenderer().render(post_serializer.data)

    return HttpResponse(json_data, content_type='application/json')

    # return JsonResponse(post_serializer.data, safe=False)

@csrf_exempt
def post_create(request):
    if(request.method == 'POST'):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = PostSerializer(data=pythondata)

        if(serializer.is_valid()):
            serializer.save()
            res = {'msg': 'Post Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def post_update(request):
    if(request.method == 'PUT'):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        post = Post.objects.get(id=id)

        serializer = PostSerializer(post, data=pythondata)

        if(serializer.is_valid()):
            serializer.save()
            res = {'msg': 'Post Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def post_delete(request):
    if(request.method == 'DELETE'):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        post = Post.objects.get(id=id)

        post.delete()

        
        res = {'msg': 'Post Deleted!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
        
        



