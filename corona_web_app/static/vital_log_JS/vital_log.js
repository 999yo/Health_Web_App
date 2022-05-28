$('#table').DataTable({
  autoWidth: false,
  serverSide: true,
  processing: true,
  responsive: true,
  pageLength: 25,  // サンプルデータ量が多いため、デフォルト値を変えておく
  ajax: {
    'url': "{% url 'vital_log/vital_log' %}"
  },
  columnDefs: [
    
    {targets: 0, data: 'vital_user'},
    {targets: 1, data: 'vital_date'},
    {targets: 2, data: 'BodyTemperature'},
    {targets: 3, data: 'SpO2'},
    {targets: 4, data: 'Sbp'},
    {targets: 5, data: 'Dbp'},
    {targets: 6, data: 'Pulse'},
    {targets: 7, data: 'Dyspnea'},
    {targets: 8, data: 'ChestPain'},
    {targets: 9, data: 'Fatigue'},
    {targets: 10, data: 'Chills'},
    {targets: 11, data: 'Cough'},
    {targets: 12, data: 'RunnyNose'},
    {targets: 13, data: 'Nausea'},
    {targets: 14, data: 'Vomiting'},
    {targets: 15, data: 'Diarrhea'},
    {targets: 16, data: 'Headache'},
    {targets: 17, data: 'Stomachace'},
    {targets: 18, data: 'JointPain'},
    {targets: 19, data: 'Dysosmia'},
    {targets: 20, data: 'Dysgeusia'},
    {targets: 21, data: 'Convulsion'},



  ],
  order: [ ],
});