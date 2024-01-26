from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField

createTime = datetime.now


# Create your models here.
class GoodsCategory(models.Model):
    # 商品分类
    CATEGORY_TYPE = (
        (1, '一级类目'),
        (2, '二级类目'),
        (3, '三级类目')
    )
    name = models.CharField(max_length=30, default="", verbose_name="类别名", help_text="类别")
    code = models.CharField(max_length=30, default="", verbose_name="类别code", help_text="类别code")
    desc = models.CharField(max_length=30, default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.CharField(max_length=30, choices=CATEGORY_TYPE, verbose_name="类别目录", help_text="类别目录")
    parent_category = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, verbose_name="父类目级别",
                                        help_text="父目录",
                                        related_name="sub_cat")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=createTime, verbose_name='创建时间')

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodCategoryBrand(models.Model):
    # 品牌名
    name = models.CharField(max_length=200, default="", verbose_name="品牌名", help_text="品牌名")
    desc = models.CharField(max_length=200, default="", verbose_name="品牌描述", help_text="品牌描述")
    image = models.ImageField(max_length=200, upload_to="brands/images/")
    add_time = models.DateTimeField(default=createTime, verbose_name='创建时间')

    class Meta:
        verbose_name = '品牌名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    # 商品
    name = models.CharField(max_length=300, verbose_name="商品名")
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="商品类目")
    good_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
    click_number = models.IntegerField(default=0, verbose_name="点击数")
    sold_number = models.IntegerField(default=0, verbose_name="销售量")
    fav_number = models.IntegerField(default=0, verbose_name="收藏数")
    good_num = models.IntegerField(default=0, verbose_name="库存数")
    market_price = models.FloatField(default=0, verbose_name="市场价格")
    shop_price = models.FloatField(default=0, verbose_name="售价")
    good_brief = models.TextField(max_length=500, verbose_name="商品简短描述")
    good_des = UEditorField(verbose_name="商品描述", imagePath="goods/images/", width=1900, height=300, filePath="goods/files/", default="")
    ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, verbose_name="封面")
    goods_front_image_url = models.CharField(max_length=500, verbose_name="封面")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    add_time = models.DateTimeField(default=createTime, verbose_name='创建时间')

    class Meta:
        verbose_name = '商品名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    # 商品轮播图
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品", related_name="images")
    image = models.ImageField(upload_to="banner/images/", verbose_name="图片", null=True, blank=True)
    image_url = models.CharField(max_length=300, null=True, blank=True, verbose_name="图片url")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    # 轮播商品
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品轮播图")
    image = models.ImageField(upload_to="banner", verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name