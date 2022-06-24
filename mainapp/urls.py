from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    
    # * when you go to the home it will bring you to the same home page or when you type [home]
    path('home', views.home, name = 'home'),
    path('sign-up', views.sign_up, name = 'sign_up'),
    path('create-post', views.create_post, name = 'create_post'),
]