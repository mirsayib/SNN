from django.http import HttpResponse, JsonResponse, Http404
from blog.models import Post
from users.models import Profile
from django.contrib.auth.models import User
from .serializers import (
    BlogSerializer,
    ProfileSerializer,
    UserSerializer,
)
import io
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status, mixins, generics, permissions
from rest_framework.views import APIView

from .permissions import IsAuthorOrReadOnly

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts':reverse('post-list', request=request, format=format)
    })


class PostDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



# @api_view(['GET', 'POST'])
# def profile_list(request, format=None):
#     if(request.method=='GET'):
#         profile = Profile.objects.all()
#         profile_serializer = ProfileSerializer(profile, many=True)
#         return Response(profile_serializer.data)




class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



# @api_view(['GET', 'POST'])
# def user_list(request, format=None):
#     if(request.method=='GET'):
#         user = User.objects.all()
#         user_serializer = UserSerializer(user, many=True)
#         return Response(user_serializer.data)






# @api_view(['GET', 'POST'])
# def post_list(request, format=None):
#     if(request.method=='GET'):
#         post = Post.objects.all()
#         post_serializer = BlogSerializer(post, many=True)
#         return Response(post_serializer.data)


#     elif(request.method == 'POST'):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = PostSerializer(data=pythondata)

#         if(serializer.is_valid()):
#             serializer.save()
#             res = {'msg': 'Post Created'}
#             return Response(res, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





    

        
        



