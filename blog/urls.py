from django.urls import path
from .views import PostList, PostDetail, CreatePost, UpdatePost, DeletePost, UserPostList, SearchView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('user/<str:username>/', UserPostList.as_view(), name='user-post'),
    path('create_post/', CreatePost.as_view(), name='create'),
    path('post/<int:pk>/update_post/', UpdatePost.as_view(), name='update'),
    path('post/<int:pk>/delete_post/', DeletePost.as_view(), name='delete'),
    path('search/', SearchView.as_view(), name='search')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
