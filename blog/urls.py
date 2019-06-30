from django.urls import path
from .views import home,posts_detail,PostCreateView,PostUpdateView,PostDeleteView
urlpatterns = [
    path ('',home,name='home'),
    path ('detail/<int:post_id>/',posts_detail,name='posts_detail'),
    path('new_post/',PostCreateView.as_view(),name='new_post'),
    path ('detail/<slug:pk>/update/',PostUpdateView.as_view(),name='post_update'),
    path ('detail/<slug:pk>/delete/',PostDeleteView.as_view(),name='post_delete'),
]