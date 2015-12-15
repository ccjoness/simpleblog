from django.conf.urls import include, url
from . import views
from blog.views import CreatePost, EditPost, DeletePost

urlpatterns = [
    url(r'^$', 'blog.views.post_list', name='post_list'),
    url(r'^(?P<cat>[-\w]+)/(?P<slug>[-\w]+)/', include([
        url(r'^$', views.post_view, name='post_view'),
        url(r'^edit/$', EditPost.as_view(), name='post_edit'),
        url(r'^delete/$', DeletePost.as_view(), name='post_delete'),
    ])),
    url(r'^new/$', CreatePost.as_view(), name='post_create'),
]
