from django.urls import path
from Ecomm_app import views

urlpatterns=[
    path('home',views.home,name='home'),
    path('',views.home_page,name='home_page'),
    path('sign_up',views.sign_up,name='sign_up'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('details',views.details,name='details'),
    path('gallery',views.gallery,name='gallery'),
    path('user_signup',views.user_signup,name='user_signup'),
    path('user_home',views.user_home,name='user_home'),
    path('user_login',views.user_login,name='user_login'),




    
]