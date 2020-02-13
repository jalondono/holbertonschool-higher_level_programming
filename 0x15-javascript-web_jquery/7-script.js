$.ajax({
  url: 'https://swapi.co/api/people/5/?format=json',
  type: 'GET'
}).done(function (data) {
  $('#character').text(data.name);
});
