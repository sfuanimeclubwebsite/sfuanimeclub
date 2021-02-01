from django.urls import path

from . import views

app_name = 'sfuanime'
urlpatterns = [
    path('', views.index, name='index'),
        path('news/', views.news, name='news'),
        path('event/', views.event, name='event'),
        path('membership/', views.membership, name='membership'),
        path('gallery/', views.galleria, name='galleria'),
        path('about/', views.abouts, name='abouts'),
        path('news/<int:news_id>', views.news_index, name='news_index'),
        path('news/<str:tag_id>', views.news_tag, name='news_tag')
]
