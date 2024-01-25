from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('logins',views.logins,name="logins"),
    path('welcome_page',views.welcome_page,name="welcome_page"),
    path('signout',views.signout,name="signout")

]