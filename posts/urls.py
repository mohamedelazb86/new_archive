from django.urls import path
from . import views

app_name='posts'
urlpatterns = [
    path('base',views.base,name='base'),
    path('',views.post_list,name='post_list'),
    path('add-post',views.add_post,name='add-post'),
   
]
