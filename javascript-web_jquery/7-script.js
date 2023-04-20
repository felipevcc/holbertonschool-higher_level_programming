$(document).ready(() => {
  $.get('https://swapi-api.hbtn.io/api/people/5', data => {
    $('#character').text(data.name);
  });
});
