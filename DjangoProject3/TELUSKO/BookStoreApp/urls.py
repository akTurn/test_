from django.urls import path
from . import views
"""
urlpatterns = [
    path('', views.FstTmpView, name='index1'),
    path('books/', views.BookListView.as_view(), name='books'),
]
re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),

"""
urlpatterns = [
    path('', views.FstTmpView, name='index1'),
    path('books/', views.BookListView.as_view(), name='book-view'),
    #path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]


