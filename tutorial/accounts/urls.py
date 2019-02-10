from django.conf.urls import url
from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from . import views


app_name = 'accounts'

urlpatterns = [
url(r'^signup/$', views.signup, name='signup'),
url(r'login/$', views.login, name='login'),
# path('login/', auth_views.LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# url(r'^login/$', auth_views.auth_login, name='login',kwargs={'template_name':'accounts/login_form.html'}),
# url(r'^logout/$', auth_views.auth_logout, name='logout',kwargs={'next_page':settings.LOGIN_URL}),
url(r'^profile/$', views.profile, name='profile'),
]