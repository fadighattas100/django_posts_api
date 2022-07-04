from django.urls import path, include

urlpatterns = [
    path("django-posts-api/", include("django_posts_api.posts.api.urls")),
]
