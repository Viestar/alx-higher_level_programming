// JavaScript script that fetches and lists the title for all movies_list by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
const movieList = $("UL#list_movies")
$.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
    movieList.append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
