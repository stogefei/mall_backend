from goods.models import Goods
from django.views.generic.base import View
from django.forms.models import model_to_dict
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import json


class GoodListView(View):
    def get(self, request):
        # 通过view实现列表页
        json_list = []
        goods = Goods.objects.all()[0:10]

        # for good in goods:
        #     json_dict = {}
        #     json_dict["name"] = good.name
        #     json_dict["category"] = good.category.name
        #     json_dict["market_price"] = good.market_price
        #     json_list.append(json_dict)

        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        json_data = serializers.serialize("json", goods)
        json_data = json.loads(json_data)

        return JsonResponse(json_data, safe=False)


