from django.urls import path
from .import views

# example - 'http://example.com/posts/'
# create a new post - 'http://example.com/posts/new'
# display the number of the post by their primary key - 'http://example.com/posts/1'
# delete the number of the post by theri primaty key - 'http://example.com/posts/delete/1'

urlpatterns = [
    path('new', views.new, name='new'),
    path('<int:id>', views.detail, name='detail'),
    path('delete/<int:id>', views.delete, name='delete'),
]