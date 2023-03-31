from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('settings',views.settings,name='settings'),
    path('upload',views.upload,name='upload'),
    path('follow',views.follow,name='follow'),
    path('like-post',views.like_post,name='like-post'),
    path('search',views.search,name='search'),
    path('Profile/<str:pk>',views.Profile,name='Profile'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),

    
    
    
]