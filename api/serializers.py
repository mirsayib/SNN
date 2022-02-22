from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User
from users.models import Profile

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    date_posted = serializers.DateTimeField()

    def validate(self, data):
        if('69' in data.get('content')):
            raise serializers.ValidationError('Nice! But No!')
        
        return data

    def create(self, validate_data):
        su = User.objects.filter(is_superuser=True)[0]
        return Post.objects.create(author=su, **validate_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.date_posted = validated_data.get('date_posted', instance.date_posted)
        instance.save()
        return instance

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields='__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude=['password']


