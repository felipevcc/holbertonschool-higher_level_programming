$(document).ready(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', data => {
    $('#hello').text(data.hello);
  });
});
