$('#table').DataTable({
  ajax: {
    "processing": true,
    "dataSrc": "",
    "url": "{% url '/json' %}"
  },
  "columns": [
    
    {"data": 'id'},
    {"data": 'email'},
    {"data": 'last_name'},
    {"data": 'first_name'},
    {"data": 'last_name_kana'},
    {"data": 'first_name_kana'},
    {"data": 'birthday'},
    {"data": 'sex'},
    {"data": 'height'},
    {"data": 'weight'},
    {"data": 'phone_number'},
    {"data": 'prefecture'},
    {"data": 'emargency_contact_number'},
    {"data": 'emargency_person'},

  ]

});