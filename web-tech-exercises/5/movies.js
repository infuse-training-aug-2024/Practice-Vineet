const search_form = document.querySelector('form')
const movie_container = document.querySelector('.movie-card')
const input_box = document.querySelector('.search-bar')



const getMovieInfo = async (movie)=> {
    const apikey = "648e752c"
    const url = `https://www.omdbapi.com/?apikey=${apikey}&t=${movie}`

    //fetch returns a promisse
    const res = await fetch(url);
    const data = await res.json();

    //console.log(data);
    showMovieData(data);
}

//show data on screen
const showMovieData = (data)=>{
    const {Title, Year, Rated, Released, Runtime, Poster, Genre, Director, Actors, Plot} = data;
    const movie_element = document.createElement('div');
    movie_element.innerHTML = `
    <div class="poster-container">
            <img src="${data.Poster}" alt="${data.Title}">
        </div>
        <div class="movie-details">
            <h2>${data.Title}</h2>
            <p><strong>Year:</strong> ${data.Year}</p>
            <p><strong>Rated:</strong> ${data.Rated || 'N/A'}</p>
            <p><strong>Release Date:</strong> ${data.Released || 'N/A'}</p>
            <p><strong>Runtime:</strong> ${data.Runtime || 'N/A'}</p>
            <p><strong>Genre:</strong> ${data.Genre || 'N/A'}</p>
            <p><strong>Director:</strong> ${data.Director || 'N/A'}</p>
            <p><strong>Actors:</strong> ${data.Actors || 'N/A'}</p>
            <p><strong>Plot:</strong> ${data.Plot || 'N/A'}</p>
            <button class="view-more" data-id="${data.imdbID}">View More</button>
        </div>
    `

}

search_form.addEventListener('submit', (e)=>{
    e.preventDefault();//prevents from auto submit
    // console.log(input_box.value)
    const movie_name = input_box.value.trim(); // trim removes the spaces
    if(movie_name !== ''){
        getMovieInfo(movie_name);
    }
});