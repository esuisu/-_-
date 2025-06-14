"""
URL configuration for WebBooks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from catalog import views
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('edit1/<int:id>/', views.edit1,name='edit1'),
    path('create/', views.create,name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('author_add/', views.authors_add, name="author_add"),
    url(r'^books/$',views.BookListView.as_view(),name='books'),
    url(r'^books/(?P<pk>\d+)$',views.BookDetailView.as_view(),name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name="authors"),
    path('mybooks/',views.LoanedBooksByUserListView.as_view(),name='my-borrowed'),
    url(r'^book/create/$',views.BookCreate.as_view(),name='book_create'),
    url(r'^book/update/(?P<pk>\d+)$',views.BookUpdate.as_view(),name='book_update'),
    url(r'^book/delete/(?P<pk>\d+)$',views.BookDelete.as_view(),name='book_delete'),
]
urlpatterns += [
    path('accounts/',include('django.contrib.auth.urls')),
]
