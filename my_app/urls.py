from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns #### Static files

######### Media files
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('signup/', views.signup_page, name='signup_page'),
    path('login/', auth_views.LoginView.as_view(template_name='my_app/login_page.html'), name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='my_app/logout_page.html'), name='logout_page'),
    path('create-post/', views.create_post_page, name='create_post_page'),
    path('search/', views.search_page, name='search_page'),
    path('profile/<int:pk>', views.profile_page, name='profile_page'),
]


urlpatterns += staticfiles_urlpatterns()  ## NOTE this will check if we are in debug mode if we are it will append to urlpatterns so that it will know how to serve our static files

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    