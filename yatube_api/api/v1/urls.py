"""API app v.1 URLs."""


from django.urls import include, path
from rest_framework import routers

from .views import (CommentViewSet, FollowLightViewSet, GroupViewSet,
                    PostViewSet)

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(r'follow', FollowLightViewSet, basename='follow')


urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls))
]
