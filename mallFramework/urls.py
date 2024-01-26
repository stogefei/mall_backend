"""
URL configuration for mallFramework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# from django.contrib import admin
from mallFramework.settings import MEDIA_ROOT
from django.urls import path, re_path, include
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
# from goods.views_base import GoodListView
from goods.views import GoodsListViewSet, CategoryListViewSet

router = DefaultRouter()

router.register(r'api/goods', GoodsListViewSet, basename="goods")

router.register(r'api/category', CategoryListViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
