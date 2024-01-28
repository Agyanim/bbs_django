from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='test'),
    path('create',views.create_post,name='create'),
    path('allpost',views.all_post,name='allpost'),
    path('<str:id>',views.single_post,name="post"),
    path('update/<str:id>',views.update_post,name="update"),
    path('delete/<str:id>',views.delete_post,)
]
