from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    path('', views.indexs, name='indexs'),
    path('login', views.login, name= 'login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name= 'register'),
    path('setting', views.setting, name = 'setting'),
    path('profile/<str:pk>', views.profile, name = 'profile'),
    path('upload', views.upload, name = 'upload'), 
    path('comment', views.comment, name='comment'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('post/<str:pk>', views.post, name='post'), 
    path('follow', views.follow, name='follow'),
    path('like-post', views.like_post, name='like-post'),
    path('search_user', views.search_user, name='search_user'),
    path('search', views.search, name='search'),
    path('favourite_post/<str:pk>', views.favourite_post, name = 'favourite_post'),
    path("favourites", views.favourites, name="favourites"),
    path("view_groups", views.view_groups, name="view_groups"),
    path("create_group", views.create_group, name="create_group"),
    path("join_group", views.join_group, name="join_group"),
    path("search_group", views.search_group, name="search_group"),
    path("course_outlines", views.course_outlines, name="course_outlines"),
    path('getComments/<str:pk>/', views.getComments, name='getComments'),
    path('group_chat/<str:pk>', views.group_chat, name='group_chat'),
    path('group_chat_comment', views.group_chat_comment, name='group_chat_comment'),
    path('get_group_comments/<str:pk>/', views.get_group_comments, name='get_group_comments'),
    path("view_chats", views.view_chats, name="view_chats"), 
    path("chat/<int:user_id>", views.chat, name="chat"),
    path("send_chat_message", views.send_chat_message, name="send_chat_message"), 
    path("get_chat_message/<str:pk>", views.get_chat_message, name="get_chat_message"),
    path("student_emergency", views.student_emergency, name="student_emergency"), 
    path("notifications", views.notifications, name="notifications"), 
    path("welcome_page", views.welcome_page, name="welcome_page"), 
    
     # Forgot Password URLS
    path('forgot_password/', auth_views.PasswordResetView.as_view(template_name='forgot_password.html'), name='forgot_password'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
] 
