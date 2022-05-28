$('#table').DataTable({
  ajax: {
    "processing": true,
    "dataSrc": "",
    "url": "{% url 'data_search' %}"
  },
  "columns": [
    
    {"data": 'fields.id'},
    {"data": 'fields.last_name'},
    {"data": 'fields.first_name'},
    {"data": 'fields.last_name_kana'},
    {"data": 'fields.first_name_kana'},
    {"data": 'fields.birthday'},
    {"data": 'fields.sex'},
    {"data": 'fields.height'},
    {"data": 'fields.weight'},
    {"data": 'fields.phone_number'},
    {"data": 'fields.prefecture'},
    {"data": 'fields.emargency_contact_number'},
    {"data": 'fields.emargency_person'},

  ]

});