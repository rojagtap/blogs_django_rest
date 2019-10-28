from rest_framework import serializers
from posts.models import BlogPosts


class BlogPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPosts
        fields = '__all__'

        read_only_fields = ['user', 'pk']
