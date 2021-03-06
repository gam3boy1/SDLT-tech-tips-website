from django.urls import path
from .views import *
urlpatterns = [
  # path(¯'', views.home, name="home"),
  path('', HomeView.as_view(), name="home"),
  path('article/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
  path('add_post/', AddPostView.as_view(), name='add_post'),
  path('add_category/', AddCategoryView.as_view(), name='add_category'),
  path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
  path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
  path('category/<str:categories>/', CategoryView, name='category'),
  path('search_results', SearchResults, name='search_results'),
]