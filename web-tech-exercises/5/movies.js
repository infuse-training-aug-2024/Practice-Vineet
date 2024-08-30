const apiKey = '648e752c';
let fetchedMovies = [];
let globalSortOrder='asc';
let page=1;
let search='';
 
const fetchMovies = async (searchTerm, page=1) => {
    try {
        const response = await fetch(`https://www.omdbapi.com/?s=${searchTerm}&apikey=${apiKey}&page=${page}`);
        const data = await response.json();
 
        if (data.Response === "True") {
            if(page===1){
                fetchedMovies=data.Search;
                document.getElementById('load-more').style.display='block';
                document.getElementById('secondForm').style.display='block';
            }
            else{
                fetchedMovies=[...fetchedMovies, ...data.Search];
            }
            sortedMovies=sortMoviesByYear(fetchedMovies,globalSortOrder);
            showResults(sortedMovies);
            return fetchedMovies;
        } else {
            console.error("No movies found!");
            document.getElementById('load-more').style.display='none';
            return [];
        }
    } catch (error) {
        console.error("Error fetching movies:", error);
        return [];
    }
};
 
const sortMoviesByYear = (movies, order) => {
    if (order === 'asc') {
        return movies.sort((a, b) => parseInt(a.Year) - parseInt(b.Year));
    }
    else {
        return movies.sort((a, b) => parseInt(b.Year) - parseInt(a.Year));
    }
};
 
function showResults(movies){
    result.innerHTML='';
    movies.forEach(movie=>{
        let poster=movie.Poster;
        let title=movie.Title;
        let year=movie.Year;
        let type=movie.Type
 
        let card=document.createElement('div');
        card.className='card';
 
        let img=document.createElement('img');
        img.src=poster;
 
        let cardContent = document.createElement('div');
        cardContent.className = 'card-content';
 
        let h3=document.createElement('h3');
        h3.textContent=title;
 
        let p=document.createElement('p');
        p.innerHTML = `
            Year: ${year}<br>
            Type: ${type}
        `;
 
        let button=document.createElement('button');
        button.textContent='View Details';
        button.addEventListener('click',()=>displayMovieDetails(movie.imdbID));
 
        cardContent.appendChild(h3);
        cardContent.appendChild(p);
        cardContent.appendChild(button);
 
        card.appendChild(img);
        card.appendChild(cardContent);
 
        result.appendChild(card);
    });
}
 
function displayMovieDetails(imdbID){
    const iframe=document.getElementById('movie-info');
    iframe.src=`movie-details.html?imdbID=${imdbID}&apikey=${apiKey}`;
}
 
const form=document.querySelector('form');
const result=document.querySelector('.results');
 
form.addEventListener('submit',(e)=>{
    e.preventDefault();
    search=form.querySelector('input').value;
    page=1;
    fetchMovies(search, page).then(movies=>{
        console.log(movies);
    })
});
 
const secondForm=document.querySelector('.movie-list-section form');
secondForm.addEventListener('submit',(e)=>{
    e.preventDefault();
    let search=secondForm.querySelector('input').value;
    const filteredMovies=fetchedMovies.filter(movie=>movie.Title.toLowerCase().includes(search.toLowerCase()));
    showResults(filteredMovies);
});
 
const sortOption=document.getElementById('sort');
sortOption.addEventListener('change',()=>{
    const order=sortOption.value;
    globalSortOrder=order;
    sortedMovies=sortMoviesByYear(fetchedMovies,order);
    showResults(sortedMovies);
});
 
const loadButton=document.getElementById('load-more');
loadButton.addEventListener('click',()=>{
    page=page+1;
    fetchMovies(search, page).then(movies=>{
        console.log(movies);
    })
})