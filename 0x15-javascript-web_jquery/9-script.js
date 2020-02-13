$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'GET'
}).done((data) => {
  $('#hello').text(data.hello);
});
