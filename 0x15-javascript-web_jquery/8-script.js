$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
    const movies = data.results;
    $.each(movies, (index, movie) => {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  }
  );
});
