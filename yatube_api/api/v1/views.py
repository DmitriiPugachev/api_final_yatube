"""API app v.1 views."""


from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import filters, mixins, pagination, permissions, viewsets

from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Custom ViewSet only for POST and GET methods."""
    pass


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for posts.Group model."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet for posts.Post model."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly, ]
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        """Redefinition of perform_create method for PostViewSet."""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for posts.Comment model."""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, ]
    pagination_class = pagination.LimitOffsetPagination

    def get_queryset(self):
        """Redefinition of get_queryset method for CommentViewSet."""
        post_id = self.kwargs['post_id']
        current_post = get_object_or_404(Post, pk=post_id)
        return current_post.comments.all()

    def perform_create(self, serializer):
        """Redefinition of perform_create method for CommentViewSet."""
        post_id = self.kwargs['post_id']
        current_post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=current_post)


class FollowLightViewSet(CreateListViewSet):
    """ViewSet for posts.Follow model."""
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Redefinition of get_queryset method for FollowLightViewSet."""
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        """Redefinition of perform_create method for FollowLightViewSet."""
        serializer.save(user=self.request.user)
