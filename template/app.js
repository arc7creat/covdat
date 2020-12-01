
 var ctx = document.getElementById('myChart').getContext('2d');
 var chart = new Chart(ctx, {
   // The type of chart we want to create
   type: 'bar',

   // The data for our dataset
   data: {
       labels: {{countryname|safe}},
       datasets: [{
           label: 'Number of Confirmed Cases',
           backgroundColor: 'rgb(255, 99, 132)',
           borderColor: 'rgb(255, 99, 132)',
           data: {{barplotval|safe}}
       }]
   },

   // Configuration options go here
   options: {}
});



var ctx = document.getElementById('mysecChart').getContext('2d');
var chart = new Chart(ctx, {
  // The type of chart we want to create
  type: 'bar',

  // The data for our dataset
  data: {
      labels: {{countrynam|safe}},
      datasets: [{
          label: 'Number of Confirmed Cases',
          backgroundColor: 'rgb(255, 99, 132)',
          borderColor: 'rgb(255, 99, 132)',
          data: {{barplotval|safe}}
      }]
  },

  // Configuration options go here
  options: {}
});

document.querySelector('#countryForm').addEventListener('submit', function(e) {
e.preventDefault();
})