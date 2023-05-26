from django.urls import path

from comment.views.blog_view import BlogListCreateView, BlogDetailView

urlpatterns = [
    path("", BlogListCreateView.as_view(), name="blog_list_create"),
    path("<slug:slug>/", BlogDetailView.as_view(), name="blog_detail"),
]
