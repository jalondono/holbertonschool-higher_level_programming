const myList = $('#list_movies');
$.ajax({
  url: 'https://swapi.co/api/films/?format=json',
  type: 'GET'
}).done(function (data) {
  data.results.forEach((element) => {
    console.log(element.title);
    myList.append('<li>' + element.title + '</li>');
  });
});
