from django.urls import path

from ..views.comment_view import CommentListCreateView, CommentDetailView

urlpatterns = [
    path("", CommentListCreateView.as_view(), name="blog_list_create"),
    path("<slug:slug>/", CommentDetailView.as_view(), name="blog_detail"),
]
