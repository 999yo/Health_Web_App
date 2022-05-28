from django.views import generic
from django.views.generic import DetailView, ListView
from django_datatables_view.base_datatable_view import BaseDatatableView
from vital_input.models import Vital

class VitalList(ListView):
    model = Vital
    template_name = 'vital_log_HTML/vital_log.html'

class VitalJsonView(BaseDatatableView):
    # モデルの指定
    model = Vital
    # 表示するフィールドの指定
    columns = ['vital_date', 'BodyTemperature', 'SpO2', 'Sbp', 'Dbp', 
    'Pulse', 'Dyspnea', 'ChestPain', 'Fatigue', 'Chills',
    'Cough', 'RunnyNose','Nausea', 'Vomiting', 'Diarrhea', 
    'Headache','Stomachace','JointPain','Dysosmia', 'Dysgeusia', 'Convulsion', 'LossOfAppetite', 'MealAmount', 'AmountOfWater', 'NumberOfAntipyretics']


    def render_column(self, row, column):
        if column == 'id':
            return f'<a href="/vital_log_HTML/vital_detail/{row.id}">{row.id}</a>'
        else:
            return super(VitalJsonView, self).render_column(row, column)

    # 検索方法の指定：部分一致
    def get_filter_method(self):
        return super().FILTER_ICONTAINS

class VitalDetail(DetailView):
    model = Vital
    template_name = 'vital_log_HTML/Vital_detail.html'