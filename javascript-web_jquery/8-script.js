$(document).ready(() => {
  $.get('https://swapi-api.hbtn.io/api/films/', data => {
    $.each(data.results, (i, movie) => {
      const movieTitle = '<li>' + movie.title + '</li>';
      $('#list_movies').append(movieTitle);
    });
  });
});
