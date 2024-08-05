from rest_framework import serializers
from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['author', 'text', 'image', 'created_at', 'total_likes', 'comments']
        read_only_fields = ['author']

    
    def create(self, instance, validated_data):
        comment_data = validated_data.pop('comments')
        comment = Comment.objects.create(post=instance, **comment_data)
        return comment 
    
        
    def update(self, instance, validated_data):
        comments_data = validated_data.pop('comments')
        for comment_data in comments_data:
            comment = instance.comments.filter(id = comment_data['id'])
            comment.text = comment_data.get('text')
        
        return instance.comments
    

