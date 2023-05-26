from django.urls import path
from myblog.views import (
    create_user,
    get_user,
    update_user,
    delete_user,
    create_post,
    get_post,
    update_post,
    delete_post,
    create_like,
    get_like,
    update_like,
    delete_like,
)

urlpatterns = [
    # User URLs
    path('users/', create_user, name='create_user'),
    path('users/<int:id>/', get_user, name='get_user'),
    path('users/<int:id>/update/', update_user, name='update_user'),
    path('users/<int:id>/delete/', delete_user, name='delete_user'),

    # Post URLs
    path('posts/', create_post, name='create_post'),
    path('posts/<int:id>/', get_post, name='get_post'),
    path('posts/<int:id>/update/', update_post, name='update_post'),
    path('posts/<int:id>/delete/', delete_post, name='delete_post'),

    # Like URLs
    path('likes/', create_like, name='create_like'),
    path('likes/<int:id>/', get_like, name='get_like'),
    path('likes/<int:id>/update/', update_like, name='update_like'),
    path('likes/<int:id>/delete/', delete_like, name='delete_like'),
]
