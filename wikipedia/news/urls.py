from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name='home'),
    path("news/<int:id>/", views.detail_view, name='detail'),
    path("news/new/", views.MoviesCreateView.as_view(), name='new'),
    path('category/new/', views.CategoryCreateView.as_view(), name='category_new'),
    path('comment/new/', views.CommentCreateView.as_view(), name='comment_new'),
    path("news/<int:pk>/delete/", views.MoviesDeleteView.as_view(), name='delete'),
    path("news/<int:pk>/edit/", views.MoviesUpdateView.as_view(), name='edit'),
    path("<int:category_id>/", views.home_view, name="category"),
    path('about/', views.about, name='about'),
]