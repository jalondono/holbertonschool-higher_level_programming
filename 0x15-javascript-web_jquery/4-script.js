const divToggle = $('#toggle_header');
const header = $('header');
divToggle.click(function () {
  if (header.hasClass('green')) {
    header.addClass('red').removeClass('green');
  } else {
    header.addClass('green').removeClass('red');
  }
});
