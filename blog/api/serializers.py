from blog.models import Post
from rest_framework import serializers

class UserSerilizer(serializers.ModelSerializer):
 class Meta:
  model = Post
  fields = ['id','title','desc']