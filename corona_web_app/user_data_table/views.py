from operator import imod
from django.views import generic
from django_datatables_view.base_datatable_view import BaseDatatableView
from excel_response import ExcelMixin
from accounts.models import User
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
import sys


def user_json(request):
  users = User.objects.all()
  data = [user.get_data() for user in users]
  response = {"data": data}
  return JsonResponse(response)

def some_view(request):
    qs = User.objects.all()
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json)


    


class BaseReportView(generic.ListView):
    model = User

    # 選択データの取得
    def get_queryset(self):
        id_list = self.request.GET['id_list'].split('_')
        result = User.objects.filter(id__in=id_list)
        return result
    

class PrintView(BaseReportView):
    template_name = 'user_data_table/print.html'

class ExcelView(ExcelMixin, BaseReportView):
  
    # 見出し行を日本語にする
    def get_queryset(self):
        header = [['id', '苗字', '名前', '苗字（かな）', '名前（かな）', '生年月日', '性別', '身長',
        '体重', '電話番号', '県' , '緊急連絡先番号', '緊急連絡先']]
        body = [list(entry.values()) for entry in super().get_queryset().values()]
        return header + body


class CsvView(ExcelView):
    force_csv = True
