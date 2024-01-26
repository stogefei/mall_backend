# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer


class GoodsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin,  viewsets.GenericViewSet):
    """
        商品列表, 分页， 搜索， 过滤， 排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    pagination_class = GoodsSetPagination
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ['name', 'category']
    filterset_fields = ['id', 'category__parent_category']  # 查询外键
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def get(self, request, format=None):
    #     good = Goods.objects.all()[0:10]
    #     serializer = GoodsSerializer(good, many=True)
    #     return Response(serializer.data)


class CategoryListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
       list:
            商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
