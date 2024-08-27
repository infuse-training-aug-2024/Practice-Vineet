const fetchMovies = async (baseUrl, apiKey, page, search) => {
    try {
        const response = await fetch(`${baseUrl}?s=${search}&page=${page}&apikey=${apiKey}`);
        const data = await response.json();
        if (data.Response === 'True') {
            return data.Search.sort((a, b) => b.Year - a.Year);
        }
        return [];
    } catch (error) {
        console.error('Error fetching movies:', error);
        return [];
    }
};

const createMovieCard = (movie) => {
    const card = document.createElement('div');
    card.className = 'movie-card';

    card.innerHTML = `
        <div class="poster-container">
            <img src="${movie.Poster}" alt="${movie.Title}">
        </div>
        <div class="movie-details">
            <h2>${movie.Title}</h2>
            <p><strong>Year:</strong> ${movie.Year}</p>
            <p><strong>Rated:</strong> ${movie.Rated || 'N/A'}</p>
            <p><strong>Release Date:</strong> ${movie.Released || 'N/A'}</p>
            <p><strong>Runtime:</strong> ${movie.Runtime || 'N/A'}</p>
            <p><strong>Genre:</strong> ${movie.Genre || 'N/A'}</p>
            <p><strong>Director:</strong> ${movie.Director || 'N/A'}</p>
            <p><strong>Actors:</strong> ${movie.Actors || 'N/A'}</p>
            <p><strong>Plot:</strong> ${movie.Plot || 'N/A'}</p>
            <button class="view-more" data-id="${movie.imdbID}">View More</button>
        </div>
    `;

    return card;
};

export { fetchMovies, createMovieCard };
