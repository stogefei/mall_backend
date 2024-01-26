from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from goods.models import Goods

User = get_user_model()
createTime = datetime.now

# Create your models here.
class ShoppingCart(models.Model):
    # 购物车
    user = models.ForeignKey(User, on_delete=models.CASCADE,  verbose_name="用户")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品")
    goods_num = models.IntegerField(default=0, verbose_name="购买数量")
    add_time = models.DateTimeField(default=createTime, verbose_name='创建时间')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.goods_num)


class OrderInfo(models.Model):
    # 订单
    ORDER_STATUS = (
        ("success", "成功"),
        ("cancel", "取消"),
        ("pending", "待支付"),
    )
    PAY_TYPE = (
        ("alipay", "支付宝"),
        ("wechat", "微信"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    order_sn = models.CharField(max_length=30, verbose_name="订单编号")
    # nonce_str = models.CharField(max_length=50, null=True, blank=True, verbose_name="随机")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="交易单号")
    pay_status = models.CharField(max_length=10, choices=ORDER_STATUS, null=True, blank=True, verbose_name="支付状态")
    post_script = models.CharField(max_length=200, verbose_name="订单留言")
    order_mount = models.FloatField(default=0.0, verbose_name="订单金额")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")
    # 用户信息
    address = models.CharField(max_length=100, default="", verbose_name="收货地址")
    signer_name = models.CharField(max_length=100, default="", verbose_name="签收人")
    signer_mobile = models.CharField(max_length=11, default="", verbose_name="手机号")
    add_time = models.DateTimeField(default=createTime, verbose_name='创建时间')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    # 订单商品详情
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name="订单信息")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品")
    goods_num = models.IntegerField(default=0, verbose_name="商品数量")
    add_time = models.DateTimeField(default=createTime, verbose_name='创建时间')

    class Meta:
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)

