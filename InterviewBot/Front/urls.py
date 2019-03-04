from django.urls import path
from Front import views

app_name='Front'

urlpatterns=[
    path('register/',views.register,name="register"),
    path('user_login/',views.user_login,name="user_login"),

]
