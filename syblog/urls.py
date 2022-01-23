from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from friend import views as friend_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('register/', user_views.register, name="register"),
    path('profile/', user_views.profile, name="profile"),
    path('friends/', friend_views.friends, name="list-friends"),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('user/<int:pk>/', user_views.display_user, name="user_display"),
    path('user/<int:pk>/request_friend/', friend_views.send_request, name="friend-request"),
    path('pending_requests/', friend_views.pending_requests, name='pending-requests'),
    path('accept_request/<int:pk>/', friend_views.accept_request, name='accept-request'),
    path('decline_request/<int:pk>/', friend_views.decline_request, name='decline-request'),
    path('remove_friend/<int:pk>/', friend_views.unfriend, name='unfriend'),
    path('', include('blog.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

