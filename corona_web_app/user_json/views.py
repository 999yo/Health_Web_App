from accounts.models import User
from django.views.generic import ListView
from django_datatables_view.base_datatable_view import BaseDatatableView
from accounts.models import User
from django.urls import reverse_lazy

class UserList(ListView):
    model = User
    template_name = 'user_json.html'

class UserJsonView(BaseDatatableView):
    model = User
    success_url = reverse_lazy('user_json')
    columns = [
      'id','last_name', 'first_name', 'last_name_kana', 'first_name_kana',
      'birthday', 'sex', 'height', 'weight', 'phone_number', 
      'prefecture', 'emargency_contact_number', 'emargency_person']

    def get_filter_method(self):
        return super().FILTER_ICONTAINS

  

