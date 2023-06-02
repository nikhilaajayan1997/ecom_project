from django.urls import path
from Ecomm_app import views

urlpatterns=[
    path('home',views.home,name='home'),
    path('',views.home_page,name='home_page'),
    path('sign_up',views.sign_up,name='sign_up'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('aboutus1',views.aboutus1,name='aboutus1'),

    path('contactus',views.contactus,name='contactus'),
    path('contactus1',views.contactus1,name='contactus1'),
    path('details',views.details,name='details'),
    path('details1',views.details1,name='details1'),
    path('gallery',views.gallery,name='gallery'),
    path('user_signup',views.user_signup,name='user_signup'),
    path('user_home',views.user_home,name='user_home'),
    path('user_login',views.user_login,name='user_login'),
    path('cart',views.cart,name='cart'),




    
]