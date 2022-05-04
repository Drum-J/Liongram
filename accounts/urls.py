from django.urls import path

from .views import singup_view,login_view,logout_view

app_name = 'accounts'

urlpatterns =[
    path('signup/', singup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]