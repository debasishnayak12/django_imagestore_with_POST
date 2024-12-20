from django.urls import path
from . import views
urlpatterns = [
    path('imageupload',views.createuser, name='imageupload' ),
    path('getusers',views.getusers, name='getusers' ),
    path('getuser',views.getuser, name='getuser' )
]