from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm



urlpatterns = [
   url('', views.index, name="home"),
   url('register', views.register, name='register'),
   url('profile', views.profile, name='profile'),
   url('gram/new', views.new_post, name='new_post'),
   url('profile/edit', views.edit_profile, name='edit_profile'),
   url('<user_name>', views.users, name='user_profile'),
   url('post/<int:image_id>', views.image_view, name='image_view'),
   url('login/', auth_views.LoginView.as_view(authentication_form=LoginForm), name='login'),
   url('logout/', views.logout_view, name='logout'),
   url('search/', views.search,name='search'),
   # method views
   url('follow/<user_name>', views.follow, name='follow'),
   url('like/<int:image_id>',views.like,name='like')
]