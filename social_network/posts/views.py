from django.contrib.contenttypes.models import ContentType

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from django.shortcuts import get_object_or_404

from posts.permissions import Allowed
from rest_framework.permissions import IsAuthenticated


from posts.models import Post, Comment, Like
from posts.serializers import PostSerializer, CommentSerializer, OnePostSerializer, LikeSerializer

class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, Allowed]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = OnePostSerializer
    permission_classes = [IsAuthenticated, Allowed]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, Allowed]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class AddLikeView(APIView):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        content_type = ContentType.objects.get_for_model(Post)

        like, created = Like.objects.get_or_create(
            user=user,
            content_type=content_type,
            object_id=post.id)

        if not created:
            like.delete()
            return Response({"message": "Лайк удален"}, status=status.HTTP_200_OK)

        return Response({"message": "Лайк добавлен"}, status=status.HTTP_201_CREATED)