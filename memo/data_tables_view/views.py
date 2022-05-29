from django.views.generic import DetailView, ListView
from django_datatables_view.base_datatable_view import BaseDatatableView
from accounts.models from User


class UserInformationList(ListView):
  model = User
  template_name = 'data_tables_view_HTML/data_tables_views.html'

class UserInformationJsonView(BaseDatatableView):
  model = User
  columns = ['id','last_name', 'first_name', 'last_name_kana', 'first_name_kana',
  'birthday', 'sex', 'height', 'weight', 'phone_number', 
  'prefecture', 'emargency_contact_number', 'emargency_person']
  
  def render_column(self, row, column):
      if column == 'id':
          return f'<a href="/data_tables_view/data_datail/{row.id}">{row.id}</a>'
      else:
          return super(UserInformationJsonView, self).render_column(row, column)

  def get_filter_method(self):
    return super().FILTER_ICONTAINS

class UserInformationDetail(DetailView):
  model = User
  template_name = 'data_tables_view_HTML/data_tables_detail_.html'