from django.urls import path
from . import views

urlpatterns=[
    path('api/', views.api_view, name='api_view'),  # This is your API endpoint
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),

]