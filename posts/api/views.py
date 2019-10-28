from .serializers import BlogPostsSerializer
from posts.models import BlogPosts
from rest_framework import generics, mixins
from django.db.models import Q


class BlogPostsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BlogPostsSerializer
    #queryset = BlogPosts.objects.all()

    def get_queryset(self):
        qs = BlogPosts.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__contains=query) | Q(content__contains=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    
"""
class BlogPostsCreate(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = BlogPostsSerializer
    queryset = BlogPosts.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
"""

class BlogPostsRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = BlogPostsSerializer
    queryset = BlogPosts.objects.all()