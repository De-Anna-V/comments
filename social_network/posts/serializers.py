from rest_framework import serializers
from posts.models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user']

class OnePostSerializer(serializers.ModelSerializer):
    
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['author', 'text', 'image', 'created_at', 'total_likes', 'comments']
        read_only_fields = ['author']

     
class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['author', 'text', 'image', 'created_at', 'total_likes']
        read_only_fields = ['author']    
    

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'content_type', 'object_id']