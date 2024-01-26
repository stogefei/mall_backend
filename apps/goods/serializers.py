from rest_framework import serializers
from goods.models import Goods, GoodsCategory


class CategorySerializer2(serializers.ModelSerializer):
    """
      商品类别序列化
    """
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    """
        商品序列化
    """
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'