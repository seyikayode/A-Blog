from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PostList, PostDetail, CreatePost, UpdatePost, DeletePost, UserPostList, SearchView, handler404, handler500
urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('user/<str:username>/', UserPostList.as_view(), name='user-post'),
    path('create-post/', CreatePost.as_view(), name='create'),
    path('post/<int:pk>/update-post/', UpdatePost.as_view(), name='update'),
    path('post/<int:pk>/delete-post/', DeletePost.as_view(), name='delete'),
    path('search/', SearchView.as_view(), name='search'),
    path('error404/', handler404, name='404'),
    path('error500/', handler500, name='500')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
