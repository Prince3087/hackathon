from django.urls import path

from .views import login_view,register_view,farming_view,healthcare_view,pollution_view,private_view,recycle_view,renewable_view

urlpatterns = [
    path('login/',login_view,name='login'),
    path('register/',register_view,name='register'),
    path('farming/',farming_view,name='farming'),
    path('healthcare/',healthcare_view,name='healthcare'),
    path('pollution/',pollution_view,name='pollution'),
    path('private/',private_view,name='private'),
    path('recycle/',recycle_view,name='recycle'),
    path('renewable/',renewable_view,name='renewable'),

]
