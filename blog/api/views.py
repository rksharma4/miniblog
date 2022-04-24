from blog .models import Post
from blog.api.serializers import UserSerilizer
from rest_framework import serializers, viewsets

class UserViewSet(viewsets.ModelViewSet):
 queryset = Post.objects.all()
 serializer_class = UserSerilizer