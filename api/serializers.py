from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    date_posted = serializers.DateTimeField()

    def create(self, validate_data):
        return 

