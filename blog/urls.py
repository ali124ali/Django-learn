from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog, name = 'home'),
    path('single/', blog_single, name = 'single')
]

