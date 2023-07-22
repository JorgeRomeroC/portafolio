from django.urls import path

from blog import views
from blog.views import *

urlpatterns = [
    path('', render_posts, name='posts'),
    path('<int:post_id>', views.post_detail)
]